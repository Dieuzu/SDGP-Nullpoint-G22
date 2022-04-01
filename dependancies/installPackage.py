import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try: 
    from dependancies import installDependancy
except ImportError:
    print("\n[SYSTEM] 'setuptools' is missing!\n")
    install("setuptools")
    from dependancies import installDependancy
    print("\n[SYSTEM] Checking if any additional Dependancies needed..")
    dependance = installDependancy.iDependance
    dependance()