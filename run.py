#  import custom classes
import config
import pandas as pd


from produce_video import ProduceVideo
from music_generator import MusicGenerator
from background_generator import BackgroundGenerator
pd.options.mode.chained_assignment = None


from log_manager import LogManager

class Run:
    def __init__(self, batch):
        self.lm = LogManager(batch)
        self.mg = MusicGenerator()
        self.bg = BackgroundGenerator()
        self.bnum = self.lm.bnum

    def run_batch(self):
        #  queue videos
        i = 0
        for index, row in self.lm.log_df.iterrows():
            if row['bnum'] == self.bnum:
                self.bg.generate_video(row['pvideo'])
                self.lm.log_df['idvideo'].iloc[i] = self.bg.latest_id
            i = i + 1

        # queue and download all music
        i = 0
        for index, row in self.lm.log_df.iterrows():
            if row['bnum'] == self.bnum:
                self.mg.generate_tracks(row['pmusic'])
                self.lm.log_df['idmusic'].iloc[i] = self.mg.ids
                self.mg.download_tracks()
            i = i + 1

        #  downloads all videos
        self.bg.download_videos()
        self.lm.log_df.to_csv(self.lm.log_loc, index=False)
        pass

        #  assemble videos
        pv = ProduceVideo(log_df=self.lm.log_df,bnum=self.bnum)

run = Run({'zenscend': 2, 'spoopytunes': 2, 'happytunes': 2})
run.run_batch()
pass