import pytesseract
from PIL import Image
import easyocr 

def readimage(imagename):

    return pytesseract.image_to_string(Image.open(imagename))

print(readimage("D:\campus\download.png"))