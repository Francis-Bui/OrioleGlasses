from picamera import PiCamera
from PIL import Image, ImageOps
import pytesseract
import time
import os
import time
import RPi.GPIO as GPIO

class CodeFinished(Exception): pass

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(5,GPIO.RISING,callback=button_callback)

try:
    while True:

        def button_callback(channel):

            camera = PiCamera()
            timestr = time.strftime("%Y%m%d-%H%M%S")
            camera.capture('image/' + str(timestr))

            image = Image.open('image/' + str(timestr))
            gray = ImageOps.grayscale(image)

            #Temporarily save the grayscale file
            filename = f"{timestr}.png".format(os.getpid())
            gray.save(filename)

            #Open the grayscale file and run OCR on it
            text = pytesseract.image_to_string(Image.open(filename))
            print(text)

            raise CodeFinished

except CodeFinished:

    GPIO.cleanup()