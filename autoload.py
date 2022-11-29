# This is an autoload (singleton) which will simplify the use of gTTS

from godot import exposed, export
from godot import *

from gtts import gTTS
import pygame
from io import BytesIO


@exposed
class autoload(Node):
    def _ready(self):
        # setup pygame audio
        pygame.init()
        pygame.mixer.init()


    def say(self, text: str):
        sound = self._generate_tts(self.text)
        self._play_tts(sound)


    def _generate_tts(self, text):
        mp3_fp = BytesIO()
        tts = gTTS(text, lang='en', tld='co.uk', slow=False)
        tts.write_to_fp(mp3_fp)
        return mp3_fp


    def _play_tts(self, sound):
        pygame.mixer.music.stop()
        sound.seek(0)
        pygame.mixer.music.load(sound, "mp3")
        pygame.mixer.music.play()
