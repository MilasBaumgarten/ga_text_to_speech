extends Node


func _ready():
    # connect signal
    connect("focus_entered", self, "_on_focus_entered")


func _on_focus_entered():
    print("entered: " + str(self.text))
    
    TTS.say(str(self.text))
