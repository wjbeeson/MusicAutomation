import config
import json
import time
import httpx
import requests




class MusicGenerator():
    def __init__(self):
        #  get token to access api
        def get_pat():
            email = "wjbeeson01@gmail.com"  # @param {type:"string"}

            r = httpx.post('https://api-b2b.mubert.com/v2/GetServiceAccess',
                           json={
                               "method": "GetServiceAccess",
                               "params": {
                                   "email": email,
                                   "license": "wjbeeson01mubertlicense#ChQfdbwNes5iSXYPYdGpIEnv0ZFCEmgmActB1RM8RZutt0BLE2WLBYNbzanMCpAcMudPyqP74MC",
                                   "token": "e7e1462550e2bc10e971c95058a938bbb4e16dad",
                                   "mode": "loop"
                               }
                           })
            pass
            rdata = json.loads(r.text)
            assert rdata['status'] == 1, "probably incorrect e-mail"
            pat = rdata['data']['pat']
            print(f'Got token: {pat}')
            return pat

        def get_streams_dict():
            r = httpx.post('https://api-b2b.mubert.com/v2/GetPlayMusic',
                           json={
                               "method": "GetPlayMusic",
                               "params": {
                                   "pat": f"{self.pat}",
                               }
                           })

            #  record id to download later
            streams = {}
            rdata = json.loads(r.text)
            for category in rdata['data']['categories']:
                # print(category['Name'])
                for group in category['groups']:
                    for channel in group['channels']:
                        name = channel['name'].lower().replace(" ", "")
                        streams[name] = channel['playlist']
            return streams
        self.pat = get_pat()
        self.channel_dict = get_streams_dict()


        # instantiate id list for later
        self.ids = []


    def generate_tracks(self, streams : list, intensities : list):
        self.ids = []
        tracks_generated = 0
        while tracks_generated < config.TRACK_COUNT:
            stream = streams[tracks_generated % len(streams)]
            intensity = intensities[tracks_generated % len(intensities)]
            #  queue track generation
            print(f"Queuing track [{tracks_generated + 1}]")
            r = httpx.post('https://api-b2b.mubert.com/v2/TTMRecordTrack',
                           json={
                               "method": "TTMRecordTrack",
                               "params": {
                                   "text": f"{streams}",
                                   "pat": f"{self.pat}",
                                   "mode": f"{config.MUSIC_MODE}",
                                   "duration": f"{config.TRACK_DURATION}",
                                   "bitrate": "192"
                               }
                           })
            r = httpx.post('https://api-b2b.mubert.com/v2/RecordTrack',
                           json={
                               "method": "RecordTrack",
                               "params": {
                                   "pat": f"{self.pat}",
                                   "playlist": f"{self.channel_dict[stream]}",
                                   "duration": f"{config.TRACK_DURATION}",
                                   "format": "mp3",
                                   "intensity": f"{intensity}",
                                   "bitrate": "320",
                                   "mode": f"{config.MUSIC_MODE}"
                               }
                           })
            #  record id to download later
            rdata = json.loads(r.text)
            self.ids.append(rdata['data']['tasks'][0]['task_id'])
            tracks_generated = tracks_generated + 1

    def download_tracks(self):
        def parse_output_dict(output):
            result = {}
            tasks = output['data']['tasks']
            for task in tasks:
                id = task['task_id']
                status_code = task['task_status_code']
                dl_link = task["download_link"]
                result[id] = [status_code, dl_link]
            return result

        def download_track(id, dl_link):
            audio_file = requests.get(dl_link)
            with open(f'temp/{id}.mp3', 'wb') as f:
                f.write(audio_file.content)

        #  checks progress of downloads
        successful_dls = []
        while len(self.ids) > len(successful_dls):
            r = httpx.post('https://api-b2b.mubert.com/v2/TrackStatus',
                           json={
                               "method": "TrackStatus",
                               "params": {
                                   "pat": f"{self.pat}"
                               }
                           })

            #  converts downloads into a data structure
            print(f"Checking download progress for [{len(self.ids) - len(successful_dls)}] tracks...")
            r_dict = parse_output_dict(r.json())
            for id in self.ids:

                #  if track has already been downloaded, skip
                if successful_dls.count(id) != 0:
                    continue

                #  if track has finished downloading, download it
                assert id in r_dict.keys()
                if r_dict[id][0] == 2:
                    successful_dls.append(id)
                    download_track(id, r_dict[id][1])
            time.sleep(2)
        print("All downloads finished. Have a nice day!")





