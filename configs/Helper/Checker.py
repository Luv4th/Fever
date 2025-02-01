import requests
import socket
import threading
import time
from colorama import Fore
from datetime import datetime
current_time = datetime.now().strftime("%H:%M:%S")
WEBHOOK_URL = "Your Webhook"
MESSAGE = "Your Message"
DELAY = 0
SPAM_COUNT = 1
def send_webhook_message(webhook_url, message):
    payload = {
        "content": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(Fore.GREEN + "Message sent!")
    else:
        print(Fore.RED + "Timeout")
def spam_webhook(webhook_url, message, count, delay):
    for i in range(count):
        send_webhook_message(webhook_url, message)
        time.sleep(delay)
if __name__ == "__main__":
    print(Fore.RED + "Starting Discord webhook spammer...")
    spam_webhook(WEBHOOK_URL, MESSAGE, SPAM_COUNT, DELAY)
    print(Fore.YELLOW + "Spamming complete!")
def check_webhook(webhook_checker):
    try:
        response = requests.get(webhook_checker)
        if response.status_code == 200:
            print(Fore.GREEN + Fore.RED + "[" + current_time + "]" + Fore.LIGHTBLUE_EX + " [@" + "System" + "]" + Fore.WHITE + " | " + Fore.GREEN +  "Valid Webhook!")
        else:
            print(f"Webhook is invalid")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
def get_location(ip_address):
    token = '4344c0a5b3c5bb'
    url = f'http://ipinfo.io/{ip_address}/json?token={token}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location_info = {
            "IP": data.get("ip", "N/A"),
            "City": data.get("city", "N/A"),
            "Region": data.get("region", "N/A"),
            "Country": data.get("country", "N/A"),
            "Location (Lat, Long)": data.get("loc", "N/A"),
            "ISP/Org": data.get("org", "N/A"),
            "Postal Code": data.get("postal", "N/A"),
            "Timezone": data.get("timezone", "N/A"),
        }

        return location_info
    else:
        return {"Error": "Failed to fetch location data"}


def scan_ports_range(ip, start_port, end_port):
    port: int
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(
                Fore.GREEN + f"[{Fore.RED}{current_time}{Fore.GREEN}] {Fore.LIGHTBLUE_EX}[@System]{Fore.WHITE} | {Fore.GREEN}{Fore.BLUE}port {port} is open")
        sock.close()


def scan_ports_multithreaded(ip, start_port, end_port, num_threads):
    threads = []
    range_size = (end_port - start_port) // num_threads

    for i in range(num_threads):
        thread_start = start_port + i * range_size
        thread_end = start_port + (i + 1) * range_size - 1 if i != num_threads - 1 else end_port
        thread = threading.Thread(target=scan_ports_range, args=(ip, thread_start, thread_end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()