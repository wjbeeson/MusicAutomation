import os
import subprocess
import time
from tkinter.filedialog import askdirectory

import httpx
import json
import numpy as np
import requests
from sentence_transformers import SentenceTransformer
minilm = SentenceTransformer('all-MiniLM-L6-v2')
import ffmpeg
from IPython.display import Audio, display


pass
class MubertManager():
    def __init__(self, track_duration, track_count, loop=False):
        #  get token to access api
        def get_pat():
            email = "wjbeeson01@gmail.com" #@param {type:"string"}

            r = httpx.post('https://api-b2b.mubert.com/v2/GetServiceAccess',
                json={
                    "method":"GetServiceAccess",
                    "params": {
                        "email": email,
                        "license":"wjbeeson01mubertlicense#ChQfdbwNes5iSXYPYdGpIEnv0ZFCEmgmActB1RM8RZutt0BLE2WLBYNbzanMCpAcMudPyqP74MC",
                        "token":"e7e1462550e2bc10e971c95058a938bbb4e16dad",
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

        #  record class globals for generation
        self.track_duration = float(track_duration)
        self.track_count = track_count
        self.loop = loop

        # instantiate id list for later
        self.generation_ids = []

    def generate_tracks(self, prompt, batch):
        tracks_generated = 0
        while tracks_generated < self.track_count:
            #  queue track generation
            if self.loop:
                mode = "loop"
            else:
                mode = "track"
            print(f"Queuing track [{tracks_generated}] in batch [{batch}]")
            r = httpx.post('https://api-b2b.mubert.com/v2/TTMRecordTrack',
                           json={
                               "method": "TTMRecordTrack",
                               "params": {
                                   "text": f"{prompt}",
                                   "pat": f"{self.pat}",
                                   "mode": f"{mode}",
                                   "duration": f"{self.track_duration}",
                                   "bitrate": "192"
                               }
                           })

            #  record id to download later
            rdata = json.loads(r.text)
            self.generation_ids.append(rdata['data']['tasks'][0]['task_id'])
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
        while len(self.generation_ids) > len(successful_dls):
            r = httpx.post('https://api-b2b.mubert.com/v2/TrackStatus',
               json={
                   "method": "TrackStatus",
                   "params": {
                       "pat": f"{self.pat}"
                   }
               })

            #  converts downloads into a data structure
            print(f"Checking download progress for [{len(self.generation_ids) - len(successful_dls)}] tracks...")
            r_dict = parse_output_dict(r.json())
            for id in self.generation_ids:

                #  if track has already been downloaded, skip
                if successful_dls.count(id) != 0:
                    continue

                #  if track has finished downloading, download it
                assert id in r_dict.keys()
                if r_dict[id][0] == 2:
                    successful_dls.append(id)
                    download_track(id, r_dict[id][1])
            time.sleep(1)
        print("All downloads finished. Have a nice day!")
    def concat_tracks(self):
        def get_list_from_directory(directory=""):
            file_list = []
            if directory == "":
                directory = askdirectory()
            for file in os.listdir(directory):
                abs_path = f"{directory}\\{file}"
                split = file.split(".")
                if split[len(split) - 1] != "ini":
                    file_list.append(abs_path)
            return file_list

        #  get relative abs paths to files
        file_list = get_list_from_directory("temp")

        #  turn files into ffmpeg inputs
        audio_inputs = []
        fade_in_sec = 5
        fade_out_sec = 12

        for file in file_list:
            audio_inputs.append(
                ffmpeg
                .input(file)
                .filter(filter_name="atrim",start=0,duration=self.track_duration)
                .filter(filter_name="afade",type="in",start_time=0,duration=fade_in_sec,curve="losi")
                .filter(filter_name="afade", type="out", start_time=self.track_duration-fade_out_sec, duration=fade_out_sec, curve="par")
                .filter(filter_name="atrim", start=0, duration=self.track_duration)
            )
        pass
        (
            ffmpeg
            .concat(*audio_inputs, v=0, a=1)
            .output('done/output.mp3')
            .run(overwrite_output=True)
        )
        pass



#  start of driver code

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
f = open("batch_info", "w")

for prompt in prompts:
    mm = MubertManager(track_duration=track_duration, track_count=track_count)
    mm.concat_tracks()
    mm.generate_tracks(prompt=prompt, batch=batch)

    mm.download_tracks()
    #  TODO: Add ability for multiple outputs
    #  TODO: Add temp clearing abilities / log to know which files go in final
    #  TODO: Compile config settings into a .ini file

    batch = batch + 1


