from PIL import Image, ImageOps
import pytesseract
import argparse
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
args = vars(ap.parse_args())

#Open the test image
image = Image.open(args["image"])

#Convert the image to grayscale
gray = ImageOps.grayscale(image)

#Temporarily save the grayscale file
filename = "{}.png".format(os.getpid())
gray.save(filename)

#Open the grayscale file and run OCR on it
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)