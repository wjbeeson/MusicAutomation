import os
import urllib
from tkinter import Image
from urllib.request import urlretrieve
import replicate
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
    def __init__(self, animation_prompts):
        def _get_filename():
            filename = ""
            for i, word in enumerate(self.prompt):
                split = word.split(" ")
                for token in split:
                    filename = filename + str.title(token)
                if i < len(self.prompt) - 1:
                    filename = filename + "_"
            pass
            files = os.listdir("tmp")
            names = []

            for file in files:
                names.append(file.split('_')[0])

            next_name = -1
            while True:
                next_name = next_name + 1
                if str(next_name) not in names:
                    break
            filename = str(next_name) + '_' + filename
            filename = f"tmp/{filename}.png"
            return filename

        def _convert_prompt(animation_prompts):
            temp_prompt = ""
            for i, animation_prompt in enumerate(animation_prompts.keys()):
                key = animation_prompt
                value = animation_prompts[key]
                if i != 0:
                    temp_prompt = temp_prompt + " | "
                temp_prompt = temp_prompt + f"{key}: {value}"
            return temp_prompt

        self.prompt = _convert_prompt(animation_prompts)
        self.filename = _get_filename()

    def queue_video(self):
        model = replicate.models.get("deforum-art/deforum-stable-diffusion")
        version = model.versions.get("652b0fed80b8c0845b20de06f877115f56b70b2136d02db95f163eff4b95e35d")
        print("Queue Video...")
        output = replicate.predictions.create(
            version=version,
            input=
            {
                "model_checkpoint": "Protogen_V2.2.ckpt",
                "animation_prompts": self.prompt,
                "translation_x": "0:(0)",
                "width": 128,
                "height": 128,
                "fps": 10,
                "zoom": "0:(1.04)",
                "max_frames": 100,
#               use_init=True,
#               init_image=self.filename,
#               animation_mode="2D",
#               width=1024
            }
        )
        pass

        print("Done.\n")


animation_prompts = {
    0: "cats in the style of ghibli",
    50: "epic fantasy castle in the style of ghibli",
    100: "epic fantasy town in the style of ghibli",
    150: "infinite space in the style of ghibli"
}

test = BackgroundGenerator(animation_prompts)
test.queue_video()

