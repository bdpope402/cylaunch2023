import cv2
from datetime import datetime
import numpy as np
class photo_editor:
    def __init__(self, path):
        self.image = cv2.imread(path)
        self.path = path

    def greyscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def custom_filter(self):
        self.image = cv2.Canny(self.image, 100, 200)
    
    def timestamp(self):
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,1920)
        fontScale              = 3
        fontColor              = (255,255,255)
        thickness              = 4
        lineType               = 2

        date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        cv2.putText(self.image, date_time, 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,
            thickness,
            lineType)
    
    def flip_180(self):
        self.image = cv2.rotate(self.image, cv2.ROTATE_180)

    def write(self):
        cv2.imwrite(self.path, self.image)
    
    def changeImage(self, path):
        self.image = cv2.imread(path)
        self.path = path
    
        