import json
import os
import time
from tkinter.filedialog import askdirectory
import httpx
import requests
from sentence_transformers import SentenceTransformer

import config

minilm = SentenceTransformer('all-MiniLM-L6-v2')
import ffmpeg


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

        self.pat = get_pat()


        # instantiate id list for later
        self.ids = []

    def generate_tracks(self, prompt):
        self.ids = []
        tracks_generated = 0
        while tracks_generated < config.TRACK_COUNT:
            #  queue track generation
            print(f"Queuing track [{tracks_generated + 1}]")
            r = httpx.post('https://api-b2b.mubert.com/v2/TTMRecordTrack',
                           json={
                               "method": "TTMRecordTrack",
                               "params": {
                                   "text": f"{prompt}",
                                   "pat": f"{self.pat}",
                                   "mode": f"{config.MUSIC_MODE}",
                                   "duration": f"{config.TRACK_DURATION}",
                                   "bitrate": "192"
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
            with open(f'temp_music/{id}.mp3', 'wb') as f:
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


        pass


#  start of driver code
'''
prompts = [
    'kind beaver guards life tree, stan lee, epic',
    'astronaut riding a horse',
    'winnie the pooh cooking methamphetamine',
    'vladimir lenin smoking weed with bob marley',
    'soviet retrofuturism',
    'two wasted friends high on weed are trying to navigate their way to their hostel in a big city, night, trippy',
    'an elephant levitating on a gas balloon',
    'calm music',
    'a refrigerator floating in a pond'
]
prompts = [
    'lofi calm soothing relaxation water smooth nature study'
]
track_duration = 150
track_count = 24
batch = 0
f = open("Automation_Scripts/Mubert/batch_info", "w")

for prompt in prompts:
    mm = MusicGenerator(track_duration=track_duration, track_count=track_count)

    pass
    mm.generate_tracks(prompt=prompt, batch=batch)

    mm.download_tracks()
    mm.concat_tracks()

    #  TODO: Add ability for multiple outputs
    #  TODO: Add temp_music clearing abilities / log to know which files go in final
    #  TODO: Compile config settings into a .ini file

    batch = batch + 1
'''