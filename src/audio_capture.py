import wave

import numpy as np
import sounddevice as sd

from src.utils import show_toast

# Audio settings
SAMPLE_RATE = 44100  # CD quality
DURATION = 10  # Seconds to record
OUTPUT_FILE = "temp_audio.wav"

# Default Config (Should be stored globally or in a persistent config)
DEFAULT_CONFIG = {
    "input_device": sd.default.device[0],  # Default recording device
    "channels": 1,  # Default: 1 channel (mono)
    "last_index": -1,
}


def list_audio_devices():
    """Lists available input devices."""

    devices = sd.query_devices()

    print("\n[🎤] Available Recording Devices:\n")
    for i, dev in enumerate(devices):
        if dev["max_input_channels"] > 0:  # Only show input-capable devices
            print(f"[{i}] {dev['name']} (Channels: {dev['max_input_channels']})")
    print("\n")


def switch_audio_source():
    """Switch between different recording sources dynamically"""

    devices = sd.query_devices()

    # Filter only devices with at least 1 input channel
    input_devices = [
        (i, dev) for i, dev in enumerate(devices) if dev["max_input_channels"] >= 1
    ]

    if not input_devices:
        print("❌ No input devices found!")
        return

    # Get the last used index
    last_index = DEFAULT_CONFIG.get("last_index", -1)

    # Compute next index in a circular manner
    next_index = (last_index + 1) % len(input_devices)

    # Get next device
    device_index, device_info = input_devices[next_index]

    # Update config
    DEFAULT_CONFIG["input_device"] = device_index
    DEFAULT_CONFIG["channels"] = device_info["max_input_channels"]
    DEFAULT_CONFIG["last_index"] = next_index  # Track last used index

    print(
        f"\n🔄 Switched to: {device_info['name']} (Channels: {DEFAULT_CONFIG['channels']})"
    )
    show_toast(
        f"\n🔄 Switched to: {device_info['name']} (Channels: {DEFAULT_CONFIG['channels']})"
    )


def record_audio(duration=DURATION, filename=OUTPUT_FILE):
    """Records audio from the selected source and saves it"""

    print(
        f"[🎙] Recording from: {sd.query_devices(DEFAULT_CONFIG['input_device'])['name']}"
    )
    show_toast(
        f"[🎙] Recording from: {sd.query_devices(DEFAULT_CONFIG['input_device'])['name']}"
    )
    # Select input device
    input_device = DEFAULT_CONFIG["input_device"]
    channels = DEFAULT_CONFIG["channels"]

    if input_device is None:
        input_device = sd.default.device[0]  # Auto-select default

    # Record audio
    audio_data = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=channels,
        dtype=np.int16,
        device=input_device,
    )
    sd.wait()

    # Save audio
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data.tobytes())

    print(f"[✅] Audio saved: {filename}")
    show_toast(f"[✅] Audio saved: {filename}")


if __name__ == "__main__":
    # List devices
    list_audio_devices()

    print("[⚡] Press 'Ctrl + Shift + A' to switch audio source while recording.")

    record_audio()
