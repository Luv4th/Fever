from colorama import Fore
import os
from datetime import datetime
sys = "System"
def designe(current_time, username,):
    return f"{Fore.RED}[{current_time}]{Fore.MAGENTA} [@{username}]{Fore.WHITE} {Fore.LIGHTWHITE_EX}| "
def system(current_time, ss):
    return f"{Fore.RED}[{current_time}]{Fore.MAGENTA} [@{sys}]{Fore.WHITE} {Fore.LIGHTWHITE_EX}| "
def util():
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time,
def design(current_time, ):
    return f"{current_time}"