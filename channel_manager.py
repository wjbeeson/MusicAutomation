import os.path
from os import path
import pandas as pd


class ChannelManager:
    def __init__(self, channel_table_dir="ref_tables/channel_table.csv"):
        def check_valid_path():
            if not path.exists(self._channel_loc):
                while True:
                    #answer = input(
                    #    "There is no channel table at that position. Initialize an empty one at that location? (y/n)")
                    #  TODO: remove test value
                    answer = 'y'
                    if answer.find("n") != -1:
                        raise Exception("Check your path or create a new channel table file.")
                    if answer.find("y") != -1:
                        f = open(self._channel_loc, "w")
                        self._get_new_channel_table().to_csv(f,index=False)
                        f.close()
                        break

        def get_file_lookup_ref():
            lookup_ref = {
                'action': "ref_tables/action_bag.csv",
                'adj': "ref_tables/adj_bag.csv",
                'place': "ref_tables/place_bag.csv",
                'style': "ref_tables/style_bag.csv"
            }
            return lookup_ref

        self._channel_loc = channel_table_dir
        check_valid_path()
        self._channel_df = pd.read_csv(self._channel_loc)
        self._channel_bag_indexes = {}
        self.channel_bags = {}
        self._file_lookup = get_file_lookup_ref()

    def _get_new_channel_table(self):
        df = pd.DataFrame(
            {'id': pd.Series(dtype='str'),
             'action': pd.Series(dtype='object'),
             'adj': pd.Series(dtype='object'),
             'place': pd.Series(dtype='object'),
             'style': pd.Series(dtype='object'),
             }
        )
        return df

    def add_channel(self,id,action,adj,place,style, test=False):
        if test:
            id = 'zenscend',
            action = 'general, general',
            adj = 'lofi',
            place = 'urban',
            style = 'lofi',
        df = pd.DataFrame(
            {
                'id': id,
                'action': action,
                'adj':adj,
                'place':place,
                'style':style
            }
        )
        self._channel_df = pd.concat([df, self._channel_df])
        self._channel_df.to_csv(self._channel_loc, index=False)

    def get_channel_bags(self, channel_id):
        def get_channel_bag_indexes():
            row = self._channel_df.loc[self._channel_df['id'] == f'{channel_id}']
            for c_name in list(self._file_lookup.keys()):
                self._channel_bag_indexes[c_name] = row.iloc[0][f'{c_name}']
            pass
        def get_list_from_bags():
            for key in list(self._file_lookup.keys()):
                file = self._file_lookup[key]
                df = pd.read_csv(file)
                result = []
                for index in [s.strip() for s in self._channel_bag_indexes[key].split(',')]:
                    result.extend(df[index].tolist())
                    pass
                self.channel_bags[key] = result

        get_channel_bag_indexes()
        get_list_from_bags()
        return self.channel_bags

'''
tm = ChannelManager("ref_tables/channel_table.csv")
#tm.add_channel("","","","","",test=True)
channel_bags = tm.get_channel_bags('zenscend')
pass

'''
