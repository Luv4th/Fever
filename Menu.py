import os
import subprocess
from datetime import datetime
from colorama import Fore
from configs.Helper.Designe import designe
current_time = datetime.now().strftime("%H:%M:%S")
username = os.getlogin()
option_1 = "Spammer.py"
option_2 = "Ip lookup.py"
option_3 = "portscanner.py"
config_folder = "configs"
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
title = Fore.LIGHTRED_EX + '''
                                 ▄▀▀▀█▄    ▄▀▀█▄▄▄▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
                                █  ▄▀  ▀▄ ▐  ▄▀   ▐ █   █    █ ▐  ▄▀   ▐ █   █   █ 
                                ▐ █▄▄▄▄     █▄▄▄▄▄  ▐  █    █    █▄▄▄▄▄  ▐  █▀▀█▀  
                                 █    ▐     █    ▌     █   ▄▀    █    ▌   ▄▀    █  
                                 █         ▄▀▄▄▄▄       ▀▄▀     ▄▀▄▄▄▄   █     █   
                                █          █    ▐               █    ▐   ▐     ▐   
                               ▐          ▐                    ▐                  


                              Spammer    ip lookup   portscanner  
                               +---+       +---+       +---+       +---+      +---+
                               | 1 |       | 2 |       | 3 |       | 4 |      | 5 |
'''
print(title)
gateway = input(designe(current_time, username) + Fore.LIGHTWHITE_EX + "Select An Option : ")
if gateway == "1":
    os.chdir(config_folder)
    subprocess.run(["python", option_1])
elif gateway == "2":
    os.chdir(config_folder)
    subprocess.run(["python", option_2])
elif gateway == "3":
    os.chdir(config_folder)
    subprocess.run(["python", option_3])
else:
    print (Fore.GREEN + Fore.RED + "[" + current_time + "]" + Fore.LIGHTBLUE_EX + " [@" + "System" + "]" + Fore.WHITE + " | " + Fore.GREEN + "Invalid option! Please select 1, 2, or 3.")
    input(
        Fore.GREEN + Fore.RED + "[" + current_time + "]" + Fore.LIGHTBLUE_EX + " [@" + "System" + "]" + Fore.WHITE + " | " + Fore.GREEN + "Press Enter to exit...")