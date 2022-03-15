import pytesseract
import cv2

def readimage(img):
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread("D:\campus\yes.png")

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(readimage(img))
