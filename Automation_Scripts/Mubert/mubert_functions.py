import math
import re

import html5lib as html5lib
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import urllib.request
import random
import os
from tkinter import filedialog
from bs4 import BeautifulSoup
import requests

from selenium.webdriver.common.by import By

MAX_DOWNLOADS = 5
class Downloader():
    def __init__(self, track_count, m_duration, channels, parameters, login_path):
        self.track_count = track_count
        self.channels = channels

        #  convert parameter list to correct format
        self.prompt = ""
        for word in parameters:
            self.prompt = self.prompt + word
            self.prompt = self.prompt + " "

        #  convert sec to correct format
        min = math.floor(m_duration / 60)
        min_text = str(min)
        if len(min_text) == 1:
            min_text = "0" + min_text

        sec = m_duration % 60
        sec_text = str(sec)
        if len(sec_text) == 1:
            sec_text = "0" + sec_text
        self.duration = min_text + sec_text



        self.login_path = login_path
        self._driver = webdriver.Chrome(options=Options())

        url = "https://mubert.com/render/sign-in"
        self._driver.get(url)
        self._complete_downloads = 0
        self._active_downloads = 0
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
            #  TODO: Add support for clicking the exit button on the login banner
            login_button = self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            time.sleep(5)
            login_button.click()
            time.sleep(5)
            pass
        def _generate_tracks():
            def _click_button():
                #  find text boxes
                prompt = self._driver.find_element(By.CSS_SELECTOR, "input[name='prompt']")
                duration = self._driver.find_element(By.CSS_SELECTOR, "input[name='duration']")

                #  clear fields from garbage text
                prompt.clear()
                duration.clear()

                #  send keys
                prompt.send_keys(self.prompt)
                duration.send_keys(self.duration)
                time.sleep(1)

                pass
                generate_button = self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                generate_button.click()
                time.sleep(5)
                pass
            def _get_active_downloads():
                result = 0
                print("Reading...")
                html = self._driver.page_source
                soup = BeautifulSoup(html, "html5lib")
                rows = soup.findAll("table")[1].findAll(class_="app-table-row")
                for row in rows:
                    if len(row.find_all(id="eXtM1V8wye91")) == 1:
                        result = result + 1
                #  TODO switch back
                print(f"In Progress: [{result}]")
                return result
                #return 10

            #  initial count of active downloads
            self._driver.get("https://mubert.com/render/my-generated-tracks")
            time.sleep(5)
            self._active_downloads = _get_active_downloads()
            self._complete_downloads = -self._active_downloads

            #  start downloads
            while self._complete_downloads < self.track_count:
                pass
                #  update completed downloads
                actual_active_dls = _get_active_downloads()
                if actual_active_dls < self._active_downloads:
                    self._complete_downloads = self._complete_downloads + (self._active_downloads - actual_active_dls)
                self._active_downloads = actual_active_dls

                #  shift screen to click button until maximum downloads are queued
                if self._active_downloads < MAX_DOWNLOADS:
                    self._driver.get("https://mubert.com/render/")
                    time.sleep(5)
                    for i in range(MAX_DOWNLOADS - self._active_downloads):
                        _click_button()
                self._active_downloads = MAX_DOWNLOADS

                #  shift back to monitor screen to wait and repeat
                self._driver.get("https://mubert.com/render/my-generated-tracks")
                time.sleep(5)
            pass




            rows = self._driver.find_elements(By.CSS_SELECTOR, "tr[style*='color: ']")

        df = pd.read_csv(self.login_path)
        for index, row in df.iterrows():
            channel = row['channel']
            user = row['user']
            password = row['password']
            _login(user, password)

            _generate_tracks()


track_length = 30
track_count = 16
channels = []
parameters = ["Calm","Ambient","Zen"]
login_path = "login_info.csv"

downloader = Downloader(track_count, track_length, channels, parameters, login_path)
downloader.download_tracks()


#downloader.add_mubert_account(user, password, channel)