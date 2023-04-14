import os
from tkinter import Image
from urllib.request import urlretrieve
import replicate
from PIL import Image

'''
output = replicate.run(
    "tstramer/midjourney-diffusion:436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b",
    input={"prompt": "landscape photo, anime, aesthetic, lofi, pastel colors"}
)
print(output)
'''

def download_images(prompt, number = 1):
    def _get_filename(prompt):
        filename = ""
        for i, word in enumerate(prompt):
            split = word.split(" ")
            for token in split:
                filename = filename + str.title(token)
            if i < len(prompt) - 1:
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
        return filename

    for i in range(number):
        filename = _get_filename(prompt= prompt)
        pass
        model = replicate.models.get("tstramer/midjourney-diffusion")
        version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")

        print(f"Generating Image [{i + 1}]")
        out = version.predict(prompt=' '.join(prompt))
        urlretrieve(out[0], f"tmp/{filename}.png")
        print("Done.\n")


prompt = ["mountains", "sunset", "photorealistic", "peaceful", "anime", "japanese", "samurai", "water", "flowing", "gentle", "lofi"]
number = 3
download_images(prompt, number)