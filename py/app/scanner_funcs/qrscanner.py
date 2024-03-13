'''
A file to help scan qr codes into whatever type of sheet you are working in, it simply copys the data from the qr code,
paste, and hits the down key(this is specific for sheets). It also makes a file of all the data you have scanned
in order to avoid repeats and data loss
'''

import pyautogui
import subprocess
import time
import pyperclip
import cv2
#from ocrSeparator import VideoStream,OCR
import winsound
import threading
class VideoStream:
    def __init__(self, src):
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_EXPOSURE, -8)
        (self.grabbed,self.frame) = self.stream.read()
        self.stopped = False
    
    def start(self):
        threading.Thread(target=self.get, args=()).start()
        return self
    
    def get(self):
        while not self.stopped:
            (self.grabbed,self.frame) = self.stream.read()
    
    def read(self):
        return self.grabbed,self.frame
            
    
    def stop_process(self):
        self.stream.release()
        self.stopped = True

class OCR:
    def __init__(self):
        self.exchange = None
        self.stopped = False
        self.img = None

    def start(self):
        threading.Thread(target=self.ocr, args=()).start()
        return self
    def set_exchange(self, video_stream):
        self.exchange = video_stream

    def read(self):
        return self.exchange.grabbed,self.img

    def stop_process(self):
        self.exchange.stream.release()
        self.stopped = True

    def ocr(self):
        while not self.stopped:
            if self.exchange is not None:
                self.img = self.exchange.frame

def openQRScanner(filePath):
    frames = VideoStream(0).start()
    cap = OCR().start()
    cap.set_exchange(frames)
    detector = cv2.QRCodeDetector()
    
    prev_qr_strs = [None]
    #QR Scanner loop, breaks when you hit 'q'
    while True:
        k = cv2.waitKey(100)
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
        with open(filePath, 'r') as file:
            lines = file.readlines()
            if (qr_str == None) or (qr_str +'\n' in lines):
                continue
        with open(filePath, 'a') as file:
            file.write(qr_str + '\n')
    
        #Paste string and beep confirmation
        print(qr_str)
        pyperclip.copy(qr_str)
        prev_qr_strs.append(qr_str)
        winsound.Beep(2500,500)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('down')
    cv2.destroyAllWindows()

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
