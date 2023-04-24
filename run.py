#  import custom classes
import config
import pandas as pd


from produce_video import ProduceVideo
from music_generator import MusicGenerator
pd.options.mode.chained_assignment = None


from log_manager import LogManager

class Run:
    def __init__(self, batch):
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

        self.lm.log_df.to_csv(self.lm.log_loc, index=False)
        pass

        #  assemble videos
        pv = ProduceVideo(log_df=self.lm.log_df,bnum=self.bnum)

run = Run({'cyberpunktunes': 5})

pass