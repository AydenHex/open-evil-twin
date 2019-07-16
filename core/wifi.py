import subprocess
from wifi import Cell

from core.interface import downInterface, upInterface
from core.models import hotspot
from core.utils import wait, information, printInterfaces, question
from colorama import Fore

def scanningInterfaces(wireless):
    print(wait + "Scanning interfaces...")
    interfaces = wireless.interfaces()
    print(information + "Our availables interfaces: \n")
    printInterfaces(interfaces)
    print("\n" + question + "Select an interface for scanning")
    interface = int(input("\n OET(" + Fore.BLUE + "~" + Fore.RESET + ")$ "))
    return interfaces, interface
#
# Description: allows to increase wifi power with custom value (max=30mW)
# Param: the interface of the wifi card
# Param: the desired power (max 30mW)
# Result: return true if increase power function succeded
#
def increaseWifiPower(interface, power):
    downInterface(interface)
    if power > 30:
        power = 30
        print("Can't set power above 30mW")
    power = str(power)
    resultRegSet = subprocess.run(["iw", "reg", "set", "BO"])
    result = subprocess.run(["iwconfig", interface, "txpower", power])
    upInterface(interface)
    if not result.returncode and not resultRegSet.returncode:
        return True
    return False

#
# Description: allow to scan nearby hotspot
# Param: string who contains the interface
# Result: Return an custom list of hotspots
#
def scanHotspots(interface):
    hotspots = []
    cells = Cell.all(interface)
    for hswifi in cells:
        hotspots.append(hotspot(hswifi.ssid, hswifi.channel, hswifi.address, hswifi.quality))
    return hotspots

