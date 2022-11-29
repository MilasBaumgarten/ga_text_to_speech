# Text 2 Speech

## Setup
- add [Godot Python](https://github.com/touilleMan/godot-python) to the project
	- restart the editor after adding the extension
- install the python pyttsx3 plugin
	- run ```addons\pythonscript\windows-64\python.exe -m ensurepip```
	- run ```addons\pythonscript\windows-64\python.exe -m pip install pygame```
	- run ```addons\pythonscript\windows-64\python.exe -m pip install gtts```

## Usage
Text to speech can be easily added using the gTTS plugin. As gTTS intends to save the audio to a file, it is recommended, to use e.g. BytesIO to store the audio in memory. For the example, pygame is used to play the audio from memory.

```py
from gtts import gTTS
import pygame
from io import BytesIO


pygame.init()
pygame.mixer.init()


def generate_tts(text):
    mp3_fp = BytesIO()
    tts = gTTS(text, lang='en', slow=False)
    tts.write_to_fp(mp3_fp)
    return mp3_fp


def play_tts(sound):
    pygame.mixer.music.stop()
    sound.seek(0)
    pygame.mixer.music.load(sound, "mp3")
    pygame.mixer.music.play()


sound = generate_tts("Hello World!")
play_tts(sound)
```