# Text 2 Speech

## Setup
- add [Godot Python](https://github.com/touilleMan/godot-python) to the project
	- restart the editor after adding the extension
- install the python pyttsx3 plugin
	- run ```addons\pythonscript\windows-64\python.exe -m ensurepip```
	- run ```addons\pythonscript\windows-64\python.exe -m pip install pyttsx3```

## Usage
Text to speech can be easily added using the pyttsx3 plugin.
```py
import pyttsx3


# initialisation
engine = pyttsx3.init()

# testing
engine.say('My first code on text-to-speech')
engine.say('Thank you, Geeksforgeeks')
engine.runAndWait()
```