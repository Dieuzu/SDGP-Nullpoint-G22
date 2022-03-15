import subprocess
import sys
import installmeV2

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    

install ("setuptools")

installmeV2.main()