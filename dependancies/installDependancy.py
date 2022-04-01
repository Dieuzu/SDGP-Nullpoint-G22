import sys
import subprocess
import pkg_resources

def iDependance():
    required = {'google', 'beautifulsoup4', 'semanticscholar', 'spacy', 'opencv-python', 'pytesseract'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        print("[SYSTEM] Found a few additional Dependancies missing\n[SYSTEM] Installing all additional Dependancies")
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        print("[SYSTEM] Sucessfully Installed all additional Dependancies")
    else:
        print("[SYSTEM] All additional Dependancies are already Installed")