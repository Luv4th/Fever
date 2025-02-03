import os
start_port = 1
end_port = 10000
num_threads = 4000
from colorama import Fore, Style
from datetime import datetime
from Helper.Design import designe
from Helper.Checker import scan_ports_multithreaded
username = os.getlogin()
current_time = datetime.now().strftime("%H:%M:%S")
Target = input(designe(current_time, username) + Fore.LIGHTWHITE_EX + "Input Target's Ip : ")
print(Fore.GREEN + "[" + Fore.RED + current_time + Fore.GREEN + "]" + Fore.LIGHTBLUE_EX + " [@" + "System" + "]" + Fore.WHITE + " | " + Fore.GREEN + f"Scanning {Target} for open ports..." + Style.RESET_ALL)
scan_ports_multithreaded(Target, start_port, end_port, num_threads)
input(Fore.GREEN + Fore.RED + "[" + current_time + "]" + Fore.LIGHTBLUE_EX + " [@" + "System" + "]" + Fore.WHITE + " | " + Fore.GREEN + "Press Enter to exit...")
