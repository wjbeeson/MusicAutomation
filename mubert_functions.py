from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import urllib.request
import random
import os
from tkinter import filedialog

from selenium.webdriver.common.by import By


class Downloader():
    def __init__(self, track_count, m_duration, channels):
        self.login_path = "login_info.csv"
        self.track_count = track_count
        self.m_duration = m_duration
        self._driver = webdriver.Chrome(options=Options())

        url = "https://mubert.com/render/sign-in"
        self._driver.get(url)
    def add_mubert_account(self, user, password, channel):
        def _initialize_login_file():
            def _create_login_table():
                df = pd.DataFrame(
                    {'channel': pd.Series(dtype='str'),
                     'user': pd.Series(dtype='str'),
                     'password': pd.Series(dtype='str')})
                return df

            df = _create_login_table()
            #  Check if login file exists
            while True:
                if os.path.isfile(self.login_path):
                    #  Check if login file is empty
                    if os.stat(self.login_path).st_size == 0:
                        #  If empty, fill with empty df
                        df.to_csv(self.login_path)
                    break
                else:
                    #  If no file, make new file
                    f = open(self.login_path, "x")
                    f.close()
            return df

        df = _initialize_login_file()

        #  TODO Implement unique checking and basic df logic
        def _check_unique(user, password, channel):
            df = pd.read_csv(self.login_path)
            if channel in df['channel'].values:
                print(f"There is already an muxer account for the channel {channel}.")

        df.loc[len(df.index)] = [channel, user, password]
        df.to_csv(self.login_path)
        pass

    def download_tracks(self):
        def _login(user, password):
            #  find input boxes for user and password
            input_user = self._driver.find_element(By.CSS_SELECTOR, "input[name='email']")
            input_password = self._driver.find_element(By.CSS_SELECTOR, "input[name='password']")
            #  fill out boxes with account info
            input_user.send_keys(user)
            input_password.send_keys(password)
            login_button = self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
        def _generate_tracks():
            self._driver.implicitly_wait(10)
            rows = self._driver.find_elements("class[type='app-table-row']")
            pass
        df = pd.read_csv(self.login_path)
        for index, row in df.iterrows():
            channel = row['channel']
            user = row['user']
            password = row['password']
            _login(user, password)
            _generate_tracks()


track_length = 225
track_count = 16
# option arg to specify the specific channels you wish to create videos for
# defaults to generating tracks for all of them
channels = []
#user = "redditlifestyle@gmail.com"
#password = "55SharedPass55^^"
#channel = "test channel"

downloader = Downloader(track_count, track_length, channels)
#downloader.add_mubert_account(user, password, channel)
downloader.download_tracks()