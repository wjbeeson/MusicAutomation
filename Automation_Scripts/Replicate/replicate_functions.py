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

def random_prompt():
    filename = "choice_pool.csv"

    df = pd.read_csv(filename)

    col1 = df.iloc[:, 0].tolist()
    col2 = df.iloc[:, 1].tolist()
    col3 = df.iloc[:, 2].tolist()
    col4 = df.iloc[:, 3].tolist()
    col5 = df.iloc[:, 4].tolist()

    global random_values
    random_value1 = random.choice(col1)
    random_value2 = random.choice(col2)
    random_value3 = random.choice(col3)
    random_value4 = random.choice(col4)
    random_value5 = random.choice(col5)

    random_values = [random_value1, random_value2, random_value3, random_value4, random_value5]
    return random_values

class BackgroundGenerator:
    def __init__(self):
        self.ids = []

    def queue_video(self, animation_prompts):
        def _convert_prompt(animation_prompts):
            temp_prompt = ""
            for i, animation_prompt in enumerate(animation_prompts.keys()):
                key = animation_prompt
                value = animation_prompts[key]
                if i != 0:
                    temp_prompt = temp_prompt + " | "
                temp_prompt = temp_prompt + f"{key}: {value}"
            return temp_prompt

        prompt = _convert_prompt(animation_prompts)
        model = replicate.models.get("deforum-art/deforum-stable-diffusion")
        version = model.versions.get("652b0fed80b8c0845b20de06f877115f56b70b2136d02db95f163eff4b95e35d")
        print("Queue Video...")
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
                "max_frames": 200,
                "animation_mode": "2D"
            }
        )
        pass
        #  add id to list to check later
        self.ids.append(json.loads(output.json())['id'])

        print("Done.\n")
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
            time.sleep(60)
        pass


animation_prompts = {
    0: "Majestic Towering Impenetrable Grandiose Imposing Ancient Regal Ornate Magnificent Stronghold Fortified Resilient Legendary Enchanting Commanding Timeless Mythical Invincible Splendid Iconic castle in the style of a paper quilling painting",
    50: "Majestic Towering Impenetrable Grandiose Imposing Ancient Regal Ornate Magnificent Stronghold Fortified Resilient Legendary Enchanting Commanding Timeless Mythical Invincible Splendid Iconic mountains in the style of a paper quilling painting",
    100: "Majestic Towering Impenetrable Grandiose Imposing Ancient Regal Ornate Magnificent Stronghold Fortified Resilient Legendary Enchanting Commanding Timeless Mythical Invincible Splendid Iconic forest in the style of a paper quilling painting",
    150: "Majestic Towering Impenetrable Grandiose Imposing Ancient Regal Ornate Magnificent Stronghold Fortified Resilient Legendary Enchanting Commanding Timeless Mythical Invincible Splendid Iconic ocean by the sea in the style of a paper quilling painting"
}

test = BackgroundGenerator()
test.queue_video(animation_prompts)
test.download_videos()


