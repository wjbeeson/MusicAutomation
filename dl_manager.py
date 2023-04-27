import math
import random
from os import path

import pandas as pd

import config

import uuid
import get_json
import json
from datetime import datetime


def get_new_log():
    return pd.DataFrame(
        {
            'bnum': pd.Series(dtype='int'),
            'rnum': pd.Series(dtype='int'),
            'id': pd.Series(dtype='string'),
            'idmusic': pd.Series(dtype='object'),
            'idvideo': pd.Series(dtype='string')
         }
    )


class Manager:
    def __init__(self, batch_dict, log_dir="ref/log.csv"):
        self.log_loc = log_dir
        #  make new log file if deleted
        if not path.exists(self.log_loc):
            f = open(self.log_loc, "w")
            get_new_log().to_csv(f, index=False)
            f.close()

        self.log_df = pd.read_csv(self.log_loc)

        def get_bnum():
            if len(self.log_df) == 0:
                return 1
            return self.log_df['bnum'].max() + 1
        self.bnum = get_bnum()

        self.batch_dict = batch_dict
        self.get_prompts()

    def get_prompts(self):
        run_number = 1

        #  for each channel listed
        for channel_id in list(self.batch_dict.keys()):

            #  fetch channel specifics
            channel_dict = config.channels_dict(channel_id)

            #  for the numbers you want to generate
            for i in range(self.batch_dict[channel_id]):
                def generate_video_prompt():
                    result = {}

                    #  pick random places
                    places_cnt = math.floor(config.FRAME_COUNT / config.DIST_BETWEEN)
                    successful = 0
                    places_picks = []
                    places_list = channel_dict['places']
                    while successful < places_cnt:
                        place_pick = random.randrange(len(places_list))

                        #  if already picked, skip
                        if places_list[place_pick] in places_picks:
                            continue
                        places_picks.append(places_list[place_pick])
                        successful = successful + 1

                    positive = channel_dict['positive']
                    negative = channel_dict['negative']
                    colors = channel_dict['colors']
                    #  pick random colors
                    color_palate = ", ".join(colors[random.randrange(len(colors))])

                    frame_count = 0
                    for place in places_picks:
                        result[str(frame_count)] = f"{color_palate}, {place}, {positive} --neg {negative}"
                        frame_count = frame_count + channel_dict['prompt_dist']
                    pass
                    return result

                video_prompt = generate_video_prompt()
                batch_id = str(uuid.uuid1())
                #  add run to df
                df = pd.DataFrame({
                    'bnum': self.bnum,
                    'rnum': run_number,
                    'id': channel_id,
                    'idmusic': [""],
                    'idvideo': batch_id
                })
                #  get json object and write to file
                batch_file = get_json.get_json(
                    prompt=video_prompt,
                    batch_name=batch_id,
                    timestring=datetime.now().strftime("%Y%m%d%H%M%S"),
                    angle=channel_dict["rotation_angle"],
                    zoom=channel_dict["zoom_speed"],
                    strength=channel_dict["strength"],
                    fps=channel_dict["fps"],
                    frames=channel_dict["frames"]
                )
                json_object = json.dumps(batch_file, indent=4)
                f = open(f"json/{batch_id}", "w")
                f.write(json_object)
                f.close()

                #  add row to log
                self.log_df = pd.concat([df, self.log_df])
                run_number = run_number + 1
        self.log_df.to_csv(self.log_loc, index=False)
        pass

'''
batches = {'zenscend': 5}
lm = LogManager(batches)
'''
