import os
import subprocess

from src.ai_model import process_transcription
from src.utils import show_toast

# Path to the Whisper executable
WHISPER_PATH = os.path.abspath("./whisper-bin-x64/whisper-cli.exe")
# Path to the Whisper model (adjust if needed)
WHISPER_MODEL = os.path.abspath("./whisper-bin-x64/models/ggml-base.en.bin")
AUDIO_FILE = "temp_audio.wav"


def transcribe_audio(audio_file=AUDIO_FILE):
    """Transcribes audio using whisper.cpp"""
    print("[📝] Transcribing audio...")
    show_toast("[📝] Transcribing audio...")
    cmd = [WHISPER_PATH, "-m", WHISPER_MODEL, "-f", audio_file, "--output-txt"]
    subprocess.run(cmd)

    with open("temp_audio.wav.txt", "r") as f:
        transcript = f.read().strip()

    print(f"[✅] Transcription: {transcript}")
    show_toast(f"[✅] Transcription: {transcript}")
    process_transcription(transcript)


if __name__ == "__main__":
    transcribe_audio()
