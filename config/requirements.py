import os

def install_package(package):
    try:
        __import__(package)
    except ImportError:
        os.system(f"pip install {package} -q")

def install_requirements():
    packages = ["termcolor", "pyqcolor", "colorama", "tqdm"]
    for package in packages:
        install_package(package)
