from godot import exposed, export
from godot import *

import pyttsx3
import threading


@exposed
class Button_Description(Button):
    engine = pyttsx3.init()

    def _ready(self):
        
        # connect signal
        self.connect("focus_entered", self, "_on_focus_entered")

    def _on_focus_entered(self):
        print("entered: " + str(self.text))
        
        threading.Thread(
            target=self._say_text_async, args=(self.text,), daemon=True
        ).start()
    
    def _say_text_async(self, text):
        if self.engine.isBusy():
            self.engine.stop()
#            self.engine.endLoop()
        
        self.engine.say(text)
#        self.engine.runAndWait()
        self.engine.startLoop()
