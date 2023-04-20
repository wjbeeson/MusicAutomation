import json
import os
import time
import urllib
from tkinter import Image
from urllib.request import urlretrieve
import replicate
import requests
from PIL import Image
import pandas as pd
import random
import base64
from tkinter import filedialog

import config


class BackgroundGenerator:
    def __init__(self):
        self.ids = []



    def generate_video(self, animation_prompts):
        self.latest_id = []
        prompt = animation_prompts
        model = replicate.models.get("deforum-art/deforum-stable-diffusion")
        version = model.versions.get("652b0fed80b8c0845b20de06f877115f56b70b2136d02db95f163eff4b95e35d")
        print("Generating Video...")
        output = replicate.predictions.create(
            version=version,
            input=
            {
                "model_checkpoint": "Protogen_V2.2.ckpt",
                "animation_prompts": prompt,
                "translation_x": "0:(0)",
                "width": 1024,
                "height": 512,
                "fps": 10,
                "zoom": "0:(1.04)",
                "max_frames": config.FRAME_COUNT,
                "animation_mode": "2D"
            }
        )
        pass
        #  add id to list to check later
        self.ids.append(json.loads(output.json())['id'])
        self.latest_id.append(json.loads(output.json())['id'])
        pass

    def download_videos(self):
        def download_video(dl_link):
            #  TODO: temp
            video_file = requests.get(dl_link)
            with open(f'temp/{id}.mp4', 'wb') as f:
                f.write(video_file.content)


        successful_downloads = []
        while len(self.ids) > len(successful_downloads):
            print("\nChecking status of downloads...")
            for id in self.ids:
                if id not in successful_downloads:
                    response = replicate.predictions.get(id)
                    status = json.loads(response.json())['status']
                    print(f"id [{id}] status is {status}")
                    if status == "succeeded":
                        dl_link = json.loads(response.json())['output']
                        download_video(dl_link)
                        successful_downloads.append(id)
            if len(self.ids) > len(successful_downloads):
                time.sleep(60)
        pass




def _convert_prompt(animation_prompts):
    temp_prompt = ""
    for i, animation_prompt in enumerate(animation_prompts.keys()):
        key = animation_prompt
        value = animation_prompts[key]
        if i != 0:
            temp_prompt = temp_prompt + " | "
        temp_prompt = temp_prompt + f"{key}: {value}"
    return temp_prompt

'''
animation_prompts = {
    0: "Majestic Towering Impenetrable Grandiose Imposing Ancient Regal Ornate Magnificent Stronghold Fortified Resilient Legendary Enchanting Commanding Timeless Mythical Invincible Splendid Iconic castle in the style of a paper quilling painting",
    50: "Majestic Towering Impenetrable Grandiose Imposing Ancient Regal Ornate Magnificent Stronghold Fortified Resilient Legendary Enchanting Commanding Timeless Mythical Invincible Splendid Iconic mountains in the style of a paper quilling painting",
    100: "Majestic Towering Impenetrable Grandiose Imposing Ancient Regal Ornate Magnificent Stronghold Fortified Resilient Legendary Enchanting Commanding Timeless Mythical Invincible Splendid Iconic forest in the style of a paper quilling painting",
    150: "Majestic Towering Impenetrable Grandiose Imposing Ancient Regal Ornate Magnificent Stronghold Fortified Resilient Legendary Enchanting Commanding Timeless Mythical Invincible Splendid Iconic ocean by the sea in the style of a paper quilling painting"
}
prompt = _convert_prompt(animation_prompts)

test = BackgroundGenerator(200)
test.queue_video(prompt)
test.download_videos()

'''