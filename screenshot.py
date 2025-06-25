import pyautogui
import time
import threading
import os
from ocr import jpn_ocr
from translation_agent import translate

def take_bounded_screenshot(x, y, width, height):
    image = pyautogui.screenshot(region=(x, y, width, height))
    file_name = '1'
    image.save("snips/" + file_name + ".png")
    
def loop_code(x, y, width, height):
    take_bounded_screenshot(x, y, width, height)
    time.sleep(0.1)
    text = jpn_ocr('snips/1.png')
    time.sleep(0.1)
    translation = translate(text)
    delete_images("snips", "1.png")
    time.sleep(0.1)
    return translation

def start_scheduling(x, y, width, height):
    threading.Thread(target=loop_code, args=(x, y, width, height), daemon=True).start()

def delete_images(folder, filename):
    file_path = os.path.join(folder, filename)
    if os.path.exists(folder):
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    else:
        print(f"The {folder} folder does not exist.")