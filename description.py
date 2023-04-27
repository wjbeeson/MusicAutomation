from random import random
import pandas as pd
import random
import openai
import os
class InfoGenerator:      #OPENAI_API_KEY = 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
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    #  TODO Parameterize
    #  max_tokens = how long the result is --> more means more cost
    #  temperature = higher temp_music is more "creative"
    def generate_text(self, prompt, max_tokens=1000, temperature=0.9):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            # stop = stop after a certain number of tokens. No reason to stop since need all tokens
            stop=None,
            temperature=temperature,
        )
        return response.choices[0].text.strip()

def random_prompt():
    filename = "Automation_Scripts/Ffmpeg/choicepool.csv"

    df = pd.read_csv(filename).dropna()

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

'''
davinci = InfoGenerator()
random_values = random_prompt()
gpt_prompt = f'"below is a list of 24 hypothetical lofi hiphop song titles that are loosely related to the ' \
             f'following themes but do not include these exact words: {", ".join(str(x) for x in random_values)}"'
song_titles = davinci.generate_text(prompt=gpt_prompt)
print(song_titles)

pass
'''