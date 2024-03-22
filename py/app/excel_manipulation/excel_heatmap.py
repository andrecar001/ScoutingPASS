'''Quick code to help create a automatically fill in cell names for a heatmap in excel'''

import pyautogui
import pyperclip
import time

MAX_VALUE = 72
rows = 6
columns = 12
totalCells = rows * columns
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

#print(pyautogui.position())
for i in range(1,totalCells+1):
    pyperclip.copy('SH_POS_' + str(i))
    pyautogui.click(x=92,y=476)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.1)
    pyautogui.hotkey('enter')
    if(i % columns != 0):
        pyautogui.hotkey('right')
        continue
    pyautogui.hotkey('down')
    for j in range(1,columns):
        pyautogui.hotkey('left')
