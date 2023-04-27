#  import custom classes
import subprocess
import time

import config
import pandas as pd
from produce import ProduceVideo
from music_gen import MusicGenerator

pd.options.mode.chained_assignment = None
import google.cloud.storage as storage

from dl_manager import Manager


class Run:
    def __init__(self, batch):
        subprocess.run("runpodctl start pod 0s5shmftxvujwh")
        self.manager = Manager(batch)
        self.music_gen = MusicGenerator()
        self.bnum = self.manager.bnum
        pass

    def run_batch(self):
        # queue and download all music
        i = 0
        for index, row in self.manager.log_df.iterrows():
            if row['bnum'] == self.bnum:
                id = row['id']
                self.music_gen.generate_tracks(
                    streams=config.channels_dict(id)['streams'],
                    intensities=config.channels_dict(id)['intensities']
                )
                self.manager.log_df['idmusic'].iloc[i] = self.music_gen.ids
                self.music_gen.download_tracks()  # music is only available for 10 min
            i = i + 1

        #  write df to csv for record keeping
        self.manager.log_df.to_csv(self.manager.log_loc, index=False)

        #  download videos from storage
        storage_client = storage.Client.from_service_account_json('ref/creds.json')

        bucket = storage_client.get_bucket('runpod-output-sync')

        completed_downloads = []
        video_ids = list(self.manager.log_df.query('bnum == @self.bnum')['idvideo'].values)
        while len(completed_downloads) < len(video_ids):
            print(f"Checking download progress of [{len(video_ids) - len(completed_downloads)} videos...]")
            for id in video_ids:
                if id in completed_downloads:
                    continue
                if storage.Blob(bucket=bucket, name=f"{id}.mp4").exists(storage_client):
                    file_cloud_loc = bucket.blob(f"{id}.mp4")
                    file_cloud_loc.download_to_filename(f"temp/{id}.mp4")
                    completed_downloads.append(id)
            if len(completed_downloads) < len(video_ids):
                time.sleep(30)

        #  stop runpod when finished
        subprocess.run("runpodctl stop pod 0s5shmftxvujwh")

        #  assemble videos
        ProduceVideo(log_df=self.manager.log_df, bnum=self.bnum)

        pass


run = Run({'zenscend': 9})
run.run_batch()
pass
