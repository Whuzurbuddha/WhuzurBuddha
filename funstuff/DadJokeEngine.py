# installed: pygame, gtts, requests

import time
import requests
import json
from gtts import gTTS
from pygame import mixer



def Joke():
    url = "https://dad-jokes.p.rapidapi.com/random/joke/png"

    headers = {
        "X-RapidAPI-Key": API-KEY FROM https://rapidapi.com,
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    response.close()

    if 'body' in data:
        setup = data['body']['setup']
        punchline = data['body']['punchline']
        
        return setup, punchline

    else:
        print("Failed to get joke data.")
        return "", ""


if __name__ == '__main__':
    setup, punchline = Joke()
    tts_setup = gTTS(text=setup, lang='en')
    tts_punchline = gTTS(text=punchline, lang='en')
    print(f"SETUP: {setup}")
    print(f"PUNCHLINE: {punchline}")
    tts_setup.save("setup.mp3")
    tts_punchline.save("punchline.mp3")

    mixer.init()
    mixer.music.load("setup.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        if True:
            continue

    time.sleep(1)
        
    mixer.music.load("punchline.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        if True:
            continue
