import os
import re
import tempfile

import easyocr
import pyautogui

from src.ai_model import process_transcription
from src.utils import show_toast

string_enclosed_in = "##"  # Match text enclosed within `#`


def capture_screenshot():
    """Takes a silent screenshot and saves it temporarily."""
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    screenshot_path = temp_file.name
    temp_file.close()

    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

    return screenshot_path


def extract_text_easyocr(image_path):
    """Extracts text from an image using EasyOCR and filters text enclosed within `#`."""

    reader = easyocr.Reader(["en"])  # Load English model
    results = reader.readtext(image_path)

    extracted_text = " ".join(text[1] for text in results)  # Combine all detected text
    print("Extracted Text:\n", extracted_text)  # Debug output

    # Regex: Match text enclosed within `#`
    pattern = rf"{re.escape(string_enclosed_in)}(.*?){re.escape(string_enclosed_in)}"

    matches = re.findall(pattern, extracted_text, re.DOTALL)

    return "\n".join(matches) if matches else None


def stealth_ocr():
    """Main function to capture screenshot, extract text, and send to LLM."""
    print("[+] Capturing screenshot...")
    show_toast("[+] Capturing screenshot...")
    image_path = capture_screenshot()

    print("[+] Extracting text using EasyOCR...")
    show_toast("[+] Extracting text using EasyOCR...")
    extracted_text = extract_text_easyocr(image_path)
    os.remove(image_path)  # Delete the temporary image after processing

    if extracted_text:
        print(f"[+] Extracted Text: {extracted_text}")
        show_toast(f"[+] Extracted Text: {extracted_text}")
        process_transcription(extracted_text)
    else:
        print("[!] No text detected.")
        show_toast("[!] No text detected.")
