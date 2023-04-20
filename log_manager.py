import random
from os import path

import pandas as pd

import channel_manager
import config
from channel_manager import ChannelManager
class LogManager:
    def __init__(self, batch_dict, log_dir="ref_tables/log.csv"):
        def check_valid_path():
            if not path.exists(self.log_loc):
                while True:
                    #answer = input(
                    #    "There is no channel table at that position. Initialize an empty one at that location? (y/n)")
                    #  TODO: remove test value
                    answer = 'y'
                    if answer.find("n") != -1:
                        raise Exception("Check your path or create a new channel table file.")
                    if answer.find("y") != -1:
                        f = open(self.log_loc, "w")
                        self._get_new_channel_table().to_csv(f,index=False)
                        f.close()
                        break
        def get_bnum():
            if len(self.log_df) == 0:
                return 1
            return self.log_df['bnum'].max() + 1


        self.batch_dict = batch_dict

        self.log_loc = log_dir
        check_valid_path()
        self.log_df = pd.read_csv(self.log_loc)
        self.bnum = get_bnum()


        self._get_prompts()
        pass
    def _get_new_channel_table(self):
        df = pd.DataFrame(
            {
                'bnum': pd.Series(dtype='int'),
                'rnum': pd.Series(dtype='int'),
                'id': pd.Series(dtype='string'),
                'pmusic': pd.Series(dtype='string'),
                'pvideo': pd.Series(dtype='string'),
                'idmusic': pd.Series(dtype='object'),
                'idvideo': pd.Series(dtype='string'),
             }
        )
        return df

    def _get_prompts(self):
        run_number = 1
        for channel_id in list(self.batch_dict.keys()):
            for run in range(self.batch_dict[channel_id]):
                cm = channel_manager.ChannelManager()
                channel_bags = cm.get_channel_bags(channel_id)
                pass
                def generate_adj_prompt(count = 5):
                    successful = 0
                    picks = []
                    music_list = list(channel_bags['adj'])
                    while successful < count:
                        pick = random.randrange(len(music_list))
                        if music_list[pick] in picks:
                            continue
                        picks.append(music_list[pick])
                        successful = successful + 1
                    return " ".join(picks)
                    pass
                def generate_video_prompt(music_prompt):
                    result = {}
                    #  prefix
                    adj_prefix = music_prompt

                    #  style
                    styles_list = list(channel_bags['style'])
                    style_pick = random.randrange(len(styles_list))
                    style_suffix = styles_list[style_pick]

                    #  places
                    places_cnt = config.FRAME_COUNT / config.DIST_BETWEEN
                    successful = 0
                    places_picks = []
                    places_list = list(channel_bags['place'])
                    while successful < places_cnt:
                        place_pick = random.randrange(len(places_list))
                        if places_list[place_pick] in places_picks:
                            continue
                        places_picks.append(places_list[place_pick])
                        successful = successful + 1


                    frame_count = 0
                    for place in places_picks:
                        prompt = ""
                        prompt = f"{adj_prefix} {place} place in the style of {style_suffix}"
                        result[frame_count] = prompt
                        frame_count = frame_count + config.DIST_BETWEEN
                    return result
                    pass
                def convert_prompt(animation_prompts):
                    temp_prompt = ""
                    for i, animation_prompt in enumerate(animation_prompts.keys()):
                        key = animation_prompt
                        value = animation_prompts[key]
                        if i != 0:
                            temp_prompt = temp_prompt + " | "
                        temp_prompt = temp_prompt + f"{key}: {value}"
                    return temp_prompt



                music_prompt = generate_adj_prompt(5)
                video_prompt = convert_prompt(generate_video_prompt(music_prompt))

                #  add run to df
                df = pd.DataFrame({
                    'bnum': self.bnum,
                    'rnum': run_number,
                    'id': channel_id,
                    'pmusic': music_prompt,
                    'pvideo': video_prompt,
                    'idmusic': [""],
                    'idvideo': "",
                })
                self.log_df = pd.concat([df, self.log_df])
                run_number = run_number + 1
        self.log_df.to_csv(self.log_loc, index=False)
        pass

'''
batches = {'zenscend': 5, 'test': 5}
lm = LogManager(batches, 800, 50)
lm._get_prompts()
'''