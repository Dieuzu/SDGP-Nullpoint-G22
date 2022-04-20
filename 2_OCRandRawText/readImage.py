def readImage(imagename):

    import pytesseract as tess
    tess.pytesseract.tesseract_cmd = r'Tesseract-OCR\\tesseract.exe'
    from PIL import Image

    img = Image.open(imagename)
    text = tess.image_to_string(img)

    f = open('input\\pimg.txt', 'w')
    f.write(text)
    f.close()