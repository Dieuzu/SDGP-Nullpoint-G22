import subprocess
import sys
import installDependancy

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    

install ("setuptools")

installDependancy.main()