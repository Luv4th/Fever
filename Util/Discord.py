import os
import subprocess
from colorama import Fore
from configs.Helper.Design import designe, util, system
current_time = util()
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
username = os.getlogin()
sys = "System"
option_1 = "Spammer.py"
config_folder = "configs"
clearscreen()
title = (
    Fore.LIGHTRED_EX +
    r"""
                                               `.  \\
                                                 \  \\
                                                  .  \\
                                                  :   .
                                                  |    .
                                                  |    :
                                                  |    |
  ..._  ___                                       |    |
 `."".`''''""--..___                              |    |
 ,-\  \             ""-...__         _____________/    |
""" +
    r"""                                                                          
 / ` " '                    `""" + '""""' + r"""                  .             
 \                                                      L
 (>                                                      \\
/                                                         \\                      | 1 |  Webhook spammer
\_    ___..---.                                            L
  `--'         '.                                           \\
                 .                                           \_
                _/`.                                           `.._
             .'     -.                                             `.
            /     __.-Y     /''''''-...___,...--------.._            |
           /   _."    |    /                ' .      \   '---..._    |
          /   /      /    /                _,. '    ,/           |   |
          \_,'     _.'   /              /''     _,-'            _|   |
                  '     /               `-----''               /     |
                  `...-'                                    `...-'
"""
)
print(title)
gateway = input(designe(username, current_time) + Fore.LIGHTWHITE_EX + "Select An Option : ")
if gateway == "1":
    os.chdir(config_folder)
    subprocess.run(["python", option_1])
else:
    print(system(current_time, sys) + "Invalid option! Please select 1, 2, or 3.")
    input(
        system(current_time, sys) + "Press Enter to exit...")