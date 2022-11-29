from godot import exposed, export
from godot import *


@exposed
class Button_Description(Button):
    def _ready(self):
        # connect signal
        self.connect("focus_entered", self, "_on_focus_entered")


    def _on_focus_entered(self):
        print("entered: " + str(self.text))
        
        TTS.say(str(self.text))
