import os     # This is for deleting files 
import time   # This is for Setting timers 

def residualDel(Time):
    time.sleep(Time)   # Delays for "Time" number of seconds.

    fileHunter("4_RefferenceResultGen\\test2\\", "RawSearch.txt")
    fileHunter("4_RefferenceResultGen\\test2\\", "Refined_Links.txt")
    fileHunter("4_RefferenceResultGen\\test2\\", "TaskResults.html")
    
    print ("==================================================================================================================\n")


def fileHunter(Root, Name):
    if os.path.exists(Root + Name):
        os.remove(Root + Name)
        print("[SYSTEM] Deleted the file: " + Name)
    else:
        print("[SYSTEM] The file " + Name +" does not exist")
