from picamera import PiCamera
from PIL import Image, ImageOps
import pytesseract
import time
import os
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
def button_callback(channel):

            print ("function called")
            camera = PiCamera()
            timestr = time.strftime("%Y%m%d-%H%M%S")
            path = f"image/{timestr}"
            camera.capture(path)

            image = Image.open(path)
            gray = ImageOps.grayscale(image)

            filename = f"{timestr}.png".format(os.getpid())
            gray.save(filename)

            #Open the grayscale file and run OCR on it
            text = pytesseract.image_to_string(Image.open(filename))
            print(text)

try:
    while True:
        if not 'event' in locals():
            event = GPIO.add_event_detect(5, GPIO.RISING, callback=button_callback)
        else:
            time.sleep(1)

finally:  
    GPIO.cleanup()