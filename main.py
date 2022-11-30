from picamera import PiCamera
from PIL import Image, ImageOps
from gtts import gTTS
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
            path = f"image/image{timestr}.jpg"
            camera.capture(path)

            image = Image.open(path)
            gray = ImageOps.grayscale(image)

            filename = f"{timestr}.png".format(os.getpid())
            gray.save(filename)

            text = pytesseract.image_to_string(Image.open(filename))
            audio = gTTS(text=text, lang="en", slow=False)
            print(text)

try:
    while True:
        if not 'event' in locals():
            event = GPIO.add_event_detect(5, GPIO.RISING, callback=button_callback)
        else:
            time.sleep(1)

finally:  
    GPIO.cleanup()