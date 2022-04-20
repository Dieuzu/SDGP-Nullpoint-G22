import os     # This is for deleting files 
import time   # This is for Setting timers 

def residualDel(Time):
    time.sleep(Time)   # Delays for "Time" number of seconds.

    outputSR = "output\\SearchResults\\"
    webHTML = "web\\html\\"
    
    #this is for future stuff
    inputFiles = "input\\"
    outputNLP = "output\\NLP\\"
    outputRaw = "output\\Raw\\"

    fileHunter(outputSR, "RawSearch.txt")
    fileHunter(outputSR, "Refined_Links.txt")
    fileHunter(webHTML, "TaskResults.html")
    fileHunter(inputFiles, "pdoc.txt")
    fileHunter(inputFiles, "ppdf.txt")
    fileHunter(inputFiles, "pimg.txt")
    fileHunter(outputRaw, "Task_1.txt")
    fileHunter(outputRaw, "Task_2.txt")
    fileHunter(outputRaw, "Task_3.txt")


def fileHunter(Root, Name):
    if os.path.exists(Root + Name):
        os.remove(Root + Name)
        print("[SYSTEM] Deleted the file: " + Name)
    else:
        print("[SYSTEM] The file " + Name +" does not exist")
