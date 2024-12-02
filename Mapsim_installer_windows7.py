import os
import subprocess
import urllib.request
import sys
import platform
from dotenv import load_dotenv

load_dotenv()

github_url = "git@github.com:Mpouransari/Mapsim_Device.git"  # URL in SSH format
download_path = os.path.join(os.environ["USERPROFILE"],"dev_mapsim_","gitrepo_","mapsim_","rep",
"h23423678123924000000_01111102299876",
"python-3.8.10","s",
"Mapsim_Device")

batch_file_path = os.path.join(os.environ["USERPROFILE"], "Desktop", "run_program.bat")

def install_python():
    try:
        subprocess.run(["python", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Python is already installed.")
    except subprocess.CalledProcessError:
        print("Python is not installed. Installing Python...")
        if platform.system() == "Windows":
            python_installer_url = "https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe"  # Python installer URL for Windows
            installer_path = os.path.join(os.getenv('TEMP'), "python_installer.exe")
            urllib.request.urlretrieve(python_installer_url, installer_path)
            subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
            print("Python has been successfully installed.")
        else:
            print("This script only works on Windows.")
            sys.exit(1)

def download_code():
    print(f"Downloading source code from {github_url}...")

    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Git is installed and available.")
    except subprocess.CalledProcessError:
        print("Git is not installed. Please install Git first.")
        sys.exit(1)

    try:
        subprocess.run(["git", "clone", github_url, download_path], check=True)
        print(f"Code has been successfully downloaded to {download_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        sys.exit(1)

def create_batch_file():
    batch_content = f"""
    @echo off
    python {download_path}\\Mapsim_Device_Assistance_Bot.py
    pause
    """
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write(batch_content)
    print(f"Batch file has been created on the Desktop at {batch_file_path}.")


def install():
    install_python()  
    download_code()  
    create_batch_file()  
    print("Installation completed successfully. You can now run the program by clicking on the batch file.")

if __name__ == "__main__":
    install()
