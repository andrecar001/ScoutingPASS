import pyautogui
import subprocess
import time
import pyperclip
import openpyxl


click_interval = 0.5
copied_text = ""
pyperclip.copy("")

subprocess.run('start microsoft.windows.camera:', shell=True)
new_text = ""
while(copied_text== new_text):
    time.sleep(click_interval)
    pyautogui.click(x=800,y=1700)
    new_text = pyperclip.paste()

#subprocess.run('notepad', shell=True)
time.sleep(1)
#pyautogui.hotkey('ctrl','v')

with open("stats.txt", "a") as file:
    file.write(new_text + "\n")
