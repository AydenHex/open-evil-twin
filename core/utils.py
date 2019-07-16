import subprocess
from colorama import init, Fore,  Back,  Style

warning = "["+Fore.RED+"!"+Fore.RESET+"] "
question = "["+Fore.YELLOW+"?"+Fore.RESET+"] "
information = "["+Fore.BLUE+"I"+Fore.RESET+"] "
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"] "
found = "["+Fore.GREEN+"+"+Fore.RESET+"] "
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"] "

def clear():
    subprocess.call("clear")

def printInterfaces(interfaces):
    for index, interface in enumerate(interfaces):
        print(str(index) + " - " + interface)