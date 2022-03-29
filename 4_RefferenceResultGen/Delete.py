import os     # This is for deleting files 
import time   # This is for Setting timers 

def residualDel():
    time.sleep(20)   # Delays for 20 seconds.
    
    fileHunter("4_RefferenceResultGen\\TestFolder\\", "RawSearch.txt")
    fileHunter("4_RefferenceResultGen\\TestFolder\\", "Refined_Links.txt")
    fileHunter("4_RefferenceResultGen\\TestFolder\\", "TaskResults.html")
    
    print ("==================================================================================================================\n")


def fileHunter(Root, Name):
    if os.path.exists(Root + Name):
        os.remove(Root + Name)
        print("[SYSTEM] Deleted the file: " + Name)
    else:
        print("[SYSTEM] The file " + Name +" does not exist")
