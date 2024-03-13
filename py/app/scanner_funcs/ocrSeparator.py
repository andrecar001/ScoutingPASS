import cv2
import threading
class VideoStream:
    def __init__(self, src):
        self.stream = cv2.VideoCapture(src)
        #self.stream.set(cv2.CAP_PROP_EXPOSURE, -8)
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
