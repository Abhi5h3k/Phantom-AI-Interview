import threading

import ollama
import pyperclip
import pyttsx3
import requests

from src.utils import show_toast

# Global Variables
tts_engine = None
last_response = ""  # Stores the last AI response
last_question = ""
is_speaking = False  # Tracks if TTS is playing
stop_flag = False  # Flag to stop playback safely
speech_lock = threading.Lock()  # Ensure only one thread runs at a time


def process_via_api(text):
    global last_question
    last_question = text
    # Ollama API URL
    OLLAMA_URL = "http://localhost:11434/api/generate"

    # Define the prompt
    prompt_template = "Answer briefly: {}"

    payload = {
        "model": "tinyllama",
        "prompt": prompt_template.format(text),
        "stream": False,
    }

    # Send request to Ollama
    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        generated_text = result["response"]
        print("Generated Text:", generated_text)
        show_toast("Generated Text:", generated_text)

        play_response(generated_text)

    else:
        print("Error:", response.text)


def process_transcription(text):
    """Sends transcribed text to Ollama's model and plays the response."""
    print(f"text : {text}")
    if text.strip() == "":
        return

    global last_response
    global last_question

    stop_playback()

    last_question = text

    prompt_template = "Answer briefly: {}"
    print("[🤖] Generating AI response...")
    show_toast("[🤖] Generating AI response...")

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt_template.format(text)}],
    )
    last_response = response["message"]["content"].strip()

    print(f"[🤖] AI Response: {last_response}")
    show_toast(f"[🤖] AI Response: {last_response}")
    play_response(last_response)
    pyperclip.copy(last_response)  # Copies text to clipboard


def play_response(text):
    """Converts AI response to speech and plays it in a separate thread."""
    global is_speaking, stop_flag, tts_engine

    tts_engine = pyttsx3.init()

    def speak():
        global is_speaking, stop_flag
        with speech_lock:  # Prevent multiple threads from running `runAndWait()`

            is_speaking = True
            stop_flag = False

            tts_engine.say(text)
            tts_engine.runAndWait()  # Ensures safe execution

            is_speaking = False

    if is_speaking:  # Avoid overlapping speech threads
        print("[⚠] Already speaking, wait...")
        show_toast("[⚠] Already speaking, wait...")
        return

    threading.Thread(target=speak, daemon=True).start()


def stop_playback():
    """Stops TTS playback."""
    global is_speaking, stop_flag, tts_engine
    if is_speaking:
        stop_flag = True  # Set flag to stop playback
        tts_engine.stop()
        tts_engine.endLoop()
        is_speaking = False
        print("[⏹] Playback stopped!")
        show_toast("[⏹] Playback stopped!")


def repeat_last_response():
    """Replays the last AI response."""
    global last_response
    if last_response:
        print("[🔄] Repeating last response...")
        show_toast("[🔄] Repeating last response...")
        play_response(last_response)


def reanalyze():
    global last_response
    global last_question

    prompt_template = "Rethink over my question : {last_question} , -- last provided response was not acceptable : {last_response}"
    print("[🤖] Generating AI response...")
    show_toast("[🤖] Generating AI response...")

    response = ollama.chat(
        model="tinyllama", messages=[{"role": "user", "content": prompt_template}]
    )
    last_response = response["message"]["content"].strip()

    print(f"[🤖] AI Response: {last_response}")
    show_toast(f"[🤖] AI Response: {last_response}")
    play_response(last_response)
