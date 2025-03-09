import sys
import threading
import time
import warnings

import pyautogui
import pyperclip
from win10toast import ToastNotifier

warnings.simplefilter("ignore", category=UserWarning)
sys.stderr = open("nul", "w")  # Hide error output, remove if no error is visible

# Global flag to track typing status
typing_active = False

toaster = ToastNotifier()
show_notification = False


def show_toast(msg):
    global show_notification
    if not toaster.notification_active() and show_notification:
        toaster.show_toast(
            "Phantom AI [🤖]", f"\n{msg}", duration=5
        )  # Notification stays for 5 seconds


def toggle_notification():
    global show_notification
    show_notification = not show_notification
    print(f"Show Notification : {show_notification}")


def simulate_typing():
    global typing_active
    text = pyperclip.paste()  # Get text from clipboard

    if not text:
        print("Clipboard is empty!")
        show_toast("Clipboard is empty!")
        return

    time.sleep(2)  # Wait before typing (optional)

    typing_active = True  # Set typing flag

    print("Typing started...")
    show_toast("Typing started...")
    for char in text:
        if not typing_active:  # Check if typing is stopped
            print("Typing stopped.")
            show_toast("Typing stopped.")
            return

        pyautogui.write(char)  # Type each character
        time.sleep(0.05)  # Adjust typing speed

    typing_active = False  # Reset flag when done
    print("Typing completed.")


def start_typing():
    typing_thread = threading.Thread(target=simulate_typing)
    typing_thread.start()


def stop_typing():
    global typing_active
    typing_active = False  # Set flag to stop typing
