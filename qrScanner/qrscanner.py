import pyautogui
import subprocess
import time
import pyperclip
import openpyxl
from openpyxl import Workbook, load_workbook
import cv2
from ocrSeparator import VideoStream,OCR
import winsound


frames = VideoStream(0).start()
cap = OCR().start()
cap.set_exchange(frames)
detector = cv2.QRCodeDetector()

prev_qr_strs = [None]
#QR Scanner loop, breaks when you hit 'q'
while True:
    _, frame = frames.read()
    b,img = cap.read()
    qr_str = None
    #If qr code is defective, try again
    try:
        data, bbox, b = detector.detectAndDecode(img)
    except Exception as e:
        print("Scanner Problem, please wait for it to reset")
        continue
    if data:
        #If data isn't a string, continue
        try:
            qr_str=str(data)
        except Exception as e:
            print("An Error Has Occured, Please make sure the QR code returns a string\n")
            print("5 second delay, please remove faulty QR code:\n")
            for i in range(5,0,-1):
                print(i + "\n")
            print("Resuming program...")
            continue
        
    #Open window with camera, close by pressing 'q' key
    cv2.imshow("Camera 1", frame)
    if cv2.waitKey(1) == ord("q"):
            cap.stop_process()
            frames.stop_process()
            cv2.destroyAllWindows()
            break
    #Write qr_string to allStrings, and prevent repeats
    with open('qrScanner/allStrings.txt', 'r') as file:
        lines = file.readlines()
        if (qr_str == None) or (qr_str +'\n' in lines):
            continue
    with open('qrScanner/allStrings.txt', 'a') as file:
        file.write(qr_str + '\n')

        '''    if((qr_str == None) or (qr_str in prev_qr_strs)): 
        if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            frames.stop_process()
            cap.stop_process()
            break
        continue
        '''    
    #Paste string and beep confirmation
    print(qr_str)
    pyperclip.copy(qr_str)
    prev_qr_strs.append(qr_str)
    winsound.Beep(2500,500)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('down')

time.sleep(1)

def sendToBluetoothDevice(device_name):
    print("Sending file to device...")
    pyperclip.copy('TestSheet.xlsx')
    subprocess.Popen("cmd /c start fsquirt",shell=True)
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

#Check to send to bluetooth
if input("Would you like to send to a bluetooth device (Y/N): ") == "Y":
    sendToBluetoothDevice(input("Phone Name: "))

print("Exiting Program...")
