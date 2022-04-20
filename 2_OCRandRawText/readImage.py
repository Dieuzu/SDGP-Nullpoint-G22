def readImage(imagename):

    import pytesseract as tess
    tess.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    from PIL import Image

    img = Image.open(imagename)
    text = tess.image_to_string(img)

    f = open('D:\campus\ex\p.txt', 'w')
    f.write(text)
    f.close()