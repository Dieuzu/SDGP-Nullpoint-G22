import os

Dependancies = {"setuptools", "google", "beautifulsoup4", "semanticscholar", "spacy", "opencv-python", "pytesseract"}

def uninstallDependancies(name):
    cmdString = "pip uninstall -y " + name
    print("[SYSTEM] Uninstalling " + name + " Module : \n")
    os.system(cmdString)
    print("\n[SYSTEM] Sucessfully Uninstalled " + name + " Module!\n")
    

for x in Dependancies:
    uninstallDependancies(x)
