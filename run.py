#  import custom classes
import subprocess
import time

import config
import pandas as pd
from produce_video import ProduceVideo
from music_generator import MusicGenerator
pd.options.mode.chained_assignment = None
import google.cloud.storage as storage


from log_manager import LogManager

class Run:
    def __init__(self, batch):
        subprocess.run("runpodctl start pod ia664joc9s1izi")
        self.lm = LogManager(batch)
        self.mg = MusicGenerator()
        self.bnum = self.lm.bnum


    def run_batch(self):
        # queue and download all music
        i = 0
        for index, row in self.lm.log_df.iterrows():
            if row['bnum'] == self.bnum:
                self.mg.generate_tracks(row['pmusic'])
                self.lm.log_df['idmusic'].iloc[i] = self.mg.ids
                self.mg.download_tracks()
            i = i + 1

        #  download videos from storage
        storage_client = storage.Client.from_service_account_json('creds.json')
        bucket = storage_client.get_bucket('runpod-output-sync')

        completed_downloads = []
        video_ids = list(self.lm.log_df.query('bnum == @self.bnum')['idvideo'].values)
        while len(completed_downloads) < len(video_ids):
            print(f"Checking download progress of [{len(video_ids) - len(completed_downloads)} videos...]")
            for id in video_ids:
                if id in completed_downloads:
                    continue
                if storage.Blob(bucket=bucket, name=f"{id}.mp4").exists(storage_client):
                    file_cloud_loc = bucket.blob(f"{id}.mp4")
                    file_cloud_loc.download_to_filename(f"temp_runpod/{id}.mp4")
                    completed_downloads.append(id)
            time.sleep(30)
        subprocess.run("runpodctl stop pod ia664joc9s1izi")
        #  assemble videos
        pv = ProduceVideo(log_df=self.lm.log_df,bnum=self.bnum)

        #  write df to csv for record keeping
        self.lm.log_df.to_csv(self.lm.log_loc, index=False)
        pass

run = Run({'underwater':1})
run.run_batch()
pass