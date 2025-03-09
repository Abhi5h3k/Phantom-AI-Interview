import configparser
import os

import keyboard

from src.ai_model import reanalyze, repeat_last_response, stop_playback
from src.audio_capture import (list_audio_devices, record_audio,
                               switch_audio_source)
from src.audio_transcribe import transcribe_audio
from src.clipboard_ai import process_clipboard
from src.realtime_transcriber import start_transcription, stop_transcription
from src.stealth_ocr import stealth_ocr
from src.utils import (show_toast, start_typing, stop_typing,
                       toggle_notification)

HOTKEYS = configparser.ConfigParser()
HOTKEYS.read("./config/config.ini")


def on_hotkey(action):
    """🔥 Handles keyboard shortcuts."""
    if action == "listen":
        record_audio()
        transcribe_audio()
    elif action == "real_time":
        start_transcription()
    elif action == "stop_real_time":
        stop_transcription()
    elif action == "repeat_last_response":
        print("[🔄] Repeating last response...")
        show_toast("[🔄] Repeating last response...")
        repeat_last_response()
    elif action == "stop_response_playback":
        print("[🎙] Stop AI response...")
        show_toast("[🎙] Stop AI response...")
        stop_playback()
    elif action == "reanalyze":
        print("[🔁] Reanalyzing last prompt...")
        show_toast("[🔁] Reanalyzing last prompt...")
        reanalyze()
    elif action == "switch_input_source":
        switch_audio_source()
    elif action == "toggle_notification":
        toggle_notification()
    elif action == "stealth_ocr":
        stealth_ocr()
    elif action == "simulate_typing":
        start_typing()
    elif action == "stop_typing":
        stop_typing()
    elif action == "process_clipboard":
        process_clipboard()
    elif action == "kill":
        print("[⚠] Exiting safely...")
        show_toast("[⚠] Exiting safely...")
        # Unhook all hotkeys to stop `keyboard.wait()`
        keyboard.unhook_all()

        os._exit(0)  # Force exit the script immediately


def register_hotkeys():
    """Registers global hotkeys."""
    # List devices
    list_audio_devices()

    for action, key in HOTKEYS["HOTKEYS"].items():
        keyboard.add_hotkey(key, lambda act=action: on_hotkey(act))

    print("[✅] Hotkeys registered! Listening for key presses...")
    show_toast("[✅] Hotkeys registered! Listening for key presses...")
    keyboard.wait()  # Keeps script running


if __name__ == "__main__":
    register_hotkeys()
