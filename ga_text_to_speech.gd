tool
extends EditorPlugin

var editor_interface = null


func _init():
    print("Initialising Text 2 Speech plugin")


func _notification(p_notification: int):
    match p_notification:
        NOTIFICATION_PREDELETE:
            print("Destroying TTS plugin")


func _get_plugin_name() -> String:
    return "TTS"


func _enter_tree() -> void:
    editor_interface = get_editor_interface()
    add_autoload_singleton("TTS", "res://addons/ga_text_to_speech/autoload.py")


func _exit_tree() -> void:
    remove_autoload_singleton("TTS")
