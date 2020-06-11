from PIL import Image, ImageGrab
import numpy as np
from cv2 import cv2
import pytesseract
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

x = 1396
y = 228

offx = 14
offy = 25

while True:
    orig_img = ImageGrab.grab(bbox=(x,y,x + offx,y + offy))

    np_im = np.array(orig_img)

    img = cv2.cvtColor(np_im, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(img, config="--psm 13")

    cv2.imshow('window',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    if text == "0":
        playsound("yeah.wav")
        break