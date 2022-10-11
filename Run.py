import keyboard
import pyautogui
import pyperclip
import random

listimport=[]
matching=[]
key=[]

myfile = open('C:\\Users\\Philip\\OneDrive - Sandwell College\\Vs Code\Testing\\words.txt')
read = myfile.read()
gamekeymatch = read.split("\n")
myfile.close()

while True:
    if keyboard.is_pressed("f8"):
        location = pyautogui.position()
        break

while True:
    if keyboard.is_pressed("f8"):
        pyautogui.click(location)
        pyautogui.click(location)
        pyautogui.hotkey("ctrl","c")
        paste = pyperclip.paste()
        key.clear()
        key.append(paste)
        ############################################################################### matching character string to list, aka "listimport"
        substr = str(paste)
        for i in gamekeymatch:
            if i.__contains__(substr) :
                matching.append(i)
        ranchoice = random.choice(matching)
        print(ranchoice)
        pyautogui.press("tab")
        pyautogui.write(ranchoice,interval = 0.1)
        pyautogui.press("enter")
        matching.clear()
        
        