import os
import readImage
import readWord
import readPDF
import searchtxt
import time
import Jsonfinder
import firebaseStorage
# from luxuryFeatures import Delete
import NLPFindKeyword

def autoop():
    start_time = time.time()
    print("------------------------------------- OCR Part Start Here -------------------------------------\n")
    #firebaseStorage.firebase()
    print("[SYSTEM] checking the file extention\n")
    for root,dirs,files in os.walk('input\\'):
        for file in files:
            if file.endswith('.pdf'):
                print("[SYSTEM] File found with .pdf extection\n")
                readPDF.pdfFile(os.path.join(root,file))

            elif file.endswith('.docx'):
                print("[SYSTEM] File found with .docx extection\n")
                readWord.readword(os.path.join(root,file))

            elif file.endswith('.png'):
                print("[SYSTEM] File found with .png extection\n")
                readImage.readImage(os.path.join(root,file)) 
                
    searchtxt.searchtxt()
    Jsonfinder.Jsonfinder()
    sttime = time.time() - start_time
    format_float = "{:.2f}".format(sttime)
    print("[SYSTEM] "+format_float+" Seconds took to finished OCR part\n")


    #START of Rishi's componant.....................................................................
    print ("\n===================================== NLP Keyword Extraction =====================================\n")
    directory = "output\\Raw\\" # this is the folder where u get the Raw tasks 
    taskcount = 0
    taskName = "Task_"

    taskNumber = 3 #hardcoded value set to max 3
    
    for i in range (taskNumber):
        taskcount += 1
        NLPFindKeyword.extractNLPKeys(directory, taskName, taskcount)
          
    #END of Rishi's componant.......................................................................
    
    
    # Delete.residualDel(60)
            
if __name__ == "__main__":
    autoop()
