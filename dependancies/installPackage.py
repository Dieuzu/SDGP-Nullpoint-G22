import subprocess
import sys
from dependancies import installDependancy

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    

install ("setuptools")

installDependancy.main()