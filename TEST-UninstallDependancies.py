import os

Dependancies = {"setuptools", "google", "beautifulsoup4", "semanticscholar", "spacy", "opencv-python", "pytesseract", "docx2txt", "PyPDF2"}

def uninstallDependancies(name):
    cmdString = "pip uninstall -y " + name
    print("[SYSTEM] Uninstalling " + name + " Module : \n")
    os.system(cmdString)
    print("\n[SYSTEM] Sucessfully Uninstalled " + name + " Module!\n")

def installDependancies(name):
    cmdString = "pip install " + name
    print("[SYSTEM] installing " + name + " Module : \n")
    os.system(cmdString)
    print("\n[SYSTEM] Sucessfully installed " + name + " Module!\n")    

for x in Dependancies:
    installDependancies(x)
