import os
import readImage
import readWord
import readPDF
import searchtxt

def inputfiletype():
    for root,dirs,files in os.walk('D:\campus\ex'):
        for file in files:
            if file.endswith('.pdf'):
                readPDF.pdfFile(os.path.join(root,file))
            elif file.endswith('.docx'):
                readWord.readword(os.path.join(root,file))
            elif file.endswith('.png'):
                readImage.readImage(os.path.join(root,file)) 

    searchtxt.searchtxt()
            
