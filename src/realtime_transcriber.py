import json
import queue
import threading

import sounddevice as sd
import vosk

from src.ai_model import process_transcription, stop_playback
from src.utils import show_toast

# Initialize Vosk model (download model if not available)
VOSK_MODEL_PATH = "./vosk-model-en-in-0.5"  # Update with actual path
model = vosk.Model(VOSK_MODEL_PATH)

# Queue to store audio data
audio_queue = queue.Queue()
# Flag to control transcription loop
stop_listening = threading.Event()


def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    audio_queue.put(bytes(indata))


# def transcribe_realtime():
#     """Listens to audio in real-time and transcribes it."""
#     recognizer = vosk.KaldiRecognizer(model, 16000)
#     with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
#                            channels=1, callback=callback):
#         print("[🎤] Listening....")
#         while True:
#             data = audio_queue.get()
#             if recognizer.AcceptWaveform(data):
#                 result = json.loads(recognizer.Result())
#                 transcript = result.get("text", "").strip()
#                 if transcript:
#                     print(f"[📝] You said: {transcript}")
#                     process_transcription(transcript)


def transcribe_realtime():
    """Listens to audio in real-time and transcribes it."""
    recognizer = vosk.KaldiRecognizer(model, 16000)
    with sd.RawInputStream(
        samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=callback
    ):
        print("[🎤] Listening....until you stop_transcription")
        show_toast("[🎤] Listening....until you stop_transcription")
        stop_listening.set()
        while stop_listening.is_set():  # Check stop flag
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                transcript = result.get("text", "").strip()
                if transcript:
                    print(f"[📝] You said: {transcript}")
                    show_toast(f"[📝] You said: {transcript}")
                    process_transcription(transcript)


def start_transcription():
    """Starts transcription in a separate thread."""
    transcription_thread = threading.Thread(target=transcribe_realtime, daemon=True)
    transcription_thread.start()


def stop_transcription():
    """Stops the transcription process."""
    stop_listening.clear()  # Set flag to stop loop
    print("[⏹] Stopping transcription...")
    show_toast("[⏹] Stopping transcription...")


if __name__ == "__main__":
    transcribe_realtime()
