import picamera
import time
import datetime

class MyCamera(object):

    def __init__(self):
        self.cam = picamera.PiCamera()
        self.sl = time.sleep
        self.cam.hflip = False
        self.cam.vflip = False

    def get_name(self, name=None):
        if name is None:
            return str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
        return str(name)

    def start(self):
        self.cam.start_preview()

    def stop(self):
        self.cam.stop_preview()
        self.cam.close()

    def hflip(self):
        if self.cam.hflip:
            self.cam.hflip = False
        else:
            self.cam.hflip = True

    def vflip(self):
        if self.cam.vflip:
            self.cam.vflip = False
        else:
            self.cam.vflip = True

    def shoot(self, name=None, wait=2):
        self.start()
        self.sl(wait)
        self.cam.capture(self.get_name(name)+".jpg")
        self.sl(2)
        self.stop()

    def record(self, name=None, wait=2, secs=10):
        self.start()
        self.sl(wait)
#        self.cam.
