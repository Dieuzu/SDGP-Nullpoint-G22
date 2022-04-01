import sys
import subprocess
import pkg_resources

def main():
    required = {'google', 'beautifulsoup4', 'semanticscholar', 'spacy', 'opencv-python', 'pytesseract'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        print("Sucessfully Installed the modules")

#============================================================for later
if __name__ == "__main__":
    main()    