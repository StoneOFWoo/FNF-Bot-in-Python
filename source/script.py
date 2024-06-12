import json
import threading
import keyboard
import pyautogui

i = 0
k = {}

print("TO STOP THE PROGRAM CLOSSE OUT OF THIS WINDOW!")
print("DO NOT CLICK ON THE GUI OR IT WILL CRASH!!!")

def pressKey(x, y, rgb, keybind):
    while True:
        if pyautogui.pixelMatchesColor(x, y, (rgb[0], rgb[1], rgb[2]),tolerance=20):
            keyboard.press(keybind)
        else:
            keyboard.release(keybind)

def pressKeyInvis(x, y, rgb, keybind):
    while True:
        if pyautogui.pixelMatchesColor(x, y, (rgb[0], rgb[1], rgb[2]),tolerance=20):
            keyboard.release(keybind)
            keyboard.press(keybind)

with open('source/user/user_saves.json', 'r') as openfile:

    dataofuser = json.load(openfile)
    

with open(dataofuser['lastConfig'], 'r') as openfile:
    json_object = json.load(openfile)


while i < len(json_object['arrows'][0]):
    i += 1
    if json_object['extras'][0]['trasparent_hold_notes'] == True:
        k["key{0}".format(i)] = threading.Thread(target=pressKeyInvis, args=(json_object['arrows'][0][str(i)][0]['x'], json_object['arrows'][0][str(i)][0]['y'], json_object['arrows'][0][str(i)][0]['rgb'], json_object['arrows'][0][str(i)][0]['keybind'],))
        k["key{0}".format(i)].start()
    else:
        k["key{0}".format(i)] = threading.Thread(target=pressKey, args=(json_object['arrows'][0][str(i)][0]['x'], json_object['arrows'][0][str(i)][0]['y'], json_object['arrows'][0][str(i)][0]['rgb'], json_object['arrows'][0][str(i)][0]['keybind'],))
        k["key{0}".format(i)].start()
