import os.path
from os import path
import pandas as pd


class TableManager:
    def __init__(self, channel_table_dir):

        def check_valid_path():
            if not path.exists(self.channel_loc):
                while True:
                    answer = input(
                        "There is no channel table at that position. Initialize an empty one at that location? (y/n)")
                    if answer.find("n") != -1:
                        raise Exception("Check your path or create a new channel table file.")
                    if answer.find("y") != -1:
                        f = open(self.channel_loc, "w")
                        self._get_new_channel_table().to_csv(f)
                        f.close()
                        break

        self.channel_loc = channel_table_dir
        check_valid_path()
        self.channel_df = pd.read_csv(self.channel_loc)

    def _get_new_channel_table(self):
        df = pd.DataFrame(
            {'id': pd.Series(dtype='str'),
             'action': pd.Series(dtype='object'),
             'adj': pd.Series(dtype='object'),
             'place': pd.Series(dtype='object'),
             'style': pd.Series(dtype='object'),
             'title': pd.Series(dtype='object'),
             'tstamp': pd.Series(dtype='object'),
             })
        return df

    def add_channel(self,id,action,adj,place,style,title,tstamp, test=False):
        if test:
            id = "zenscend",
            action = ["general"],
            adj = ["lofi"],
            place = ["urban"],
            style = ["lofi"],
            title = [""],
            tstamp = [""]
        df = pd.DataFrame(
            {
                "id": id,
                "action": action,
                "adj":adj,
                "place":place,
                "style":style,
                "title":title,
                "tstamp":tstamp
            }
        )
        self.channel_df = pd.concat([df,self.channel_df])
        pass


tm = TableManager("C:\\Users\\wjbee\\PycharmProjects\\Music_Automation\\Ref_Tables\\channel_table.csv")
tm.add_channel("","","","","","","",test=True)
