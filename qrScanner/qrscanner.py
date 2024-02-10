import pyautogui
import subprocess
import time
import pyperclip
import openpyxl
from openpyxl import Workbook, load_workbook
import cv2
from ocrSeparator import VideoStream,OCR


frames = VideoStream(2).start()
cap = OCR().start()
cap.set_exchange(frames)
detector = cv2.QRCodeDetector()

prev_qr_strs = [None]
#QR Scanner loop, breaks when you hit 'q'
while True:
    _, frame = frames.read()
    b,img = cap.read()
    qr_str = None
    try:
        data, bbox, b = detector.detectAndDecode(img)
    except Exception as e:
        print("Scanner Problem, please wait for it to reset")
        continue
    if data:
        try:
            qr_str=str(data)
            
        except Exception as e:
            print("An Error Has Occured, Please make sure the QR code returns a string\n")
            print("5 second delay, please remove faulty QR code:\n")
            for i in range(5,0,-1):
                print(i + "\n")
            print("Resuming program...")
            continue
    cv2.imshow("Camera 1", frame)
    if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            cap.stop_process()
            frames.stop_process()
            
            break
    if((qr_str == None) or (qr_str in prev_qr_strs)): 
        if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            frames.stop_process()
            cap.stop_process()
            break
        continue
    
    print(qr_str)
    prev_qr_strs.append(qr_str)
    pyperclip.copy(qr_str)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('down')

time.sleep(1)

def sendToBluetoothDevice(device_name):
    print("Sending file to device...")
    pyperclip.copy('TestSheet.xlsx')
    subprocess.Popen("cmd /c start fsquirt",shell=True)
    print("Clipboard")
    time.sleep(2)
    pyautogui.hotkey('s')
    time.sleep(1)
    pyautogui.hotkey('down')
    time.sleep(1)
    pyautogui.hotkey(device_name[0])
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.typewrite('TestSheet.xlsx')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1.5)
    pyautogui.hotkey('enter')
    time.sleep(5)



sendToBluetoothDevice('One')



print("Exiting Program...")
