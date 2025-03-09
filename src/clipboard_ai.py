import pyperclip

from src.ai_model import process_transcription
from src.utils import show_toast


def get_clipboard_text():
    """Get text from the clipboard."""
    try:
        return pyperclip.paste().strip()
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        return None


def process_clipboard():
    """Extract text from clipboard and send it to AI."""
    text = get_clipboard_text()
    if text:
        print("Processing clipboard text...")
        show_toast("Processing clipboard text...")
        process_transcription(text)
    else:
        show_toast("No text detected in clipboard.")
