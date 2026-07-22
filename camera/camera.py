import cv2
from picamera2 import Picamera2

class Camera:
    def __init__(self, camera_index=0, width=640, height=480):
        self.picam2 = Picamera2()
        config = self.picam2.create_preview_configuration(main={"size": (width, height)})
        self.picam2.configure(config)
        self.picam2.start()
        try:
            self.picam2.set_controls({"AfMode": 0})
        except Exception:
            pass
        self.width = width
        self.height = height

    def read(self):
        frame = self.picam2.capture_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return frame

    def release(self):
        self.picam2.stop()
