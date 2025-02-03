import os
from Helper.Checker import get_location
from Helper.Design import designe
from colorama import Fore
from datetime import datetime
username = os.getlogin()
current_time = datetime.now().strftime("%H:%M:%S")
Ip = input((designe(current_time, username) + Fore.LIGHTWHITE_EX + "Input Ip : "))
location = get_location(Ip)
print(Fore.LIGHTCYAN_EX + "\nLocation Details:")
for key, value in location.items():
    print(Fore.GREEN + Fore.RED + "[" + current_time + "]" + Fore.LIGHTBLUE_EX + " [@" + "System" + "]" +Fore.WHITE + " | " +f"{Fore.GREEN}{key}: {Fore.WHITE}{value}")
input(Fore.GREEN + Fore.RED + "[" + current_time + "]" + Fore.LIGHTBLUE_EX + " [@" + "System" + "]" + Fore.WHITE + " | " + Fore.GREEN +   "Press Enter to exit...")
