from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import urllib.request
import random
import os
from tkinter import filedialog

class Downloader():
    def __init__(self, track_count, m_duration):
        self.track_count = track_count
        self.m_duration = m_duration
        self._driver = webdriver.Chrome(options=Options())

        url = "https://mubert.com/render"
        self._driver.get(url)

    def _perform_login(self):
        
