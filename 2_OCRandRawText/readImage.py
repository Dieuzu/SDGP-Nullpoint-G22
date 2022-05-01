def readImage(imagename):
    print("------------------------------------- Image To Text Extraction Start Here -------------------------------------\n")
    import pytesseract as tess
    tess.pytesseract.tesseract_cmd = r'Tesseract-OCR\\tesseract.exe'
    from PIL import Image
    import time


    img = Image.open(imagename)
    print("[SYSTEM] Extracting data from image to text\n")
    text = tess.image_to_string(img)
    print("[SYSTEM] Writing data to a text file\n")

    f = open('input\\pimg.txt', 'w')
    f.write(text)
    f.close()
