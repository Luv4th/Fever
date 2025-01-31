import os
from colorama import Fore
from datetime import datetime
from Helper.Checker import spam_webhook, send_webhook_message, check_webhook
from Helper.Designe import designe
username = os.getlogin()
current_time = datetime.now().strftime("%H:%M:%S")
WEBHOOK_URL = input(designe(current_time, username)+ Fore.LIGHTWHITE_EX +  "Input Webhook : ")
check_webhook(WEBHOOK_URL)
MESSAGE = input(designe(current_time, username) + Fore.LIGHTWHITE_EX +  "Input Message : ")
DELAY = float(input(Fore.RED + "[" + current_time + "]" + Fore.MAGENTA + " [@" + username + "]" + Fore.WHITE + " | " + Fore.LIGHTWHITE_EX + Fore.GREEN + "Input Delay : "))
while True:
    try:
        SPAM_COUNT = int(input(Fore.RED + "[" + current_time + "]" + Fore.MAGENTA + " [@" + username + "]" + Fore.WHITE + " | " + Fore.LIGHTWHITE_EX +  "Input How Many Times The Webhook Gets Spammed : "))
        break
    except ValueError:
        print(designe(current_time, username) + "Invalid input! Please enter a valid integer.")
send_webhook_message(WEBHOOK_URL, MESSAGE)
spam_webhook(WEBHOOK_URL, MESSAGE, SPAM_COUNT, DELAY)
input("Press Enter to exit...")
