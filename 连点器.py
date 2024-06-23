import pyautogui
import keyboard
import threading

clicking = False

def click():
    global clicking
    while clicking:
        pyautogui.click()
        pyautogui.PAUSE = 0.01
def start_and_end():
    global clicking
    if clicking:        #调用一次启动子线程，再次调用取消子线程
        clicking = False
    else:
        clicking = True
        threading.Thread(target=click).start()

if __name__ == '__main__':
    keyboard.add_hotkey('r', start_and_end)
    keyboard.wait('esc')    #阻断主线程