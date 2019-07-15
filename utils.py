import subprocess
from wifi import Cell
import os


from core.models import hotspot

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
# Description: allows to restart an interface (down and up)
# Param: the interface of the wifi card
# Result: return true if restart interface function succeeded
#
def restartInterface(interface):
    resultDown = downInterface(interface)
    resultUp = upInterface(interface)
    if resultDown and resultUp:
        return True
    return False

#
# Description: allow to up an interface
# Param: string who contains the interface
# Result: Return true or false regarding if we can up the interface
#
def upInterface(interface, ip=""):
    if ip != "":
        result = subprocess.run(["ifconfig", interface, "up", ip])
    else:
        result = subprocess.run(["ifconfig", interface, "up"])

    if result.returncode:
        return False
    return True

#
# Description: allow to down an interface
# Param: string who contains the interface
# Result: Return true or false regarding if we can down the interface
#
def downInterface(interface, ip=""):
    if ip != "":
        result = subprocess.run(["ifconfig", interface, "up", ip])
    else:
        result = subprocess.run(["ifconfig", interface, "up"])

    if result.returncode:
        print("Error while down interface " + interface)
        return False
    print("Interface down succeded")
    return True

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

def stopSystemdResolved():
    result = subprocess.run(["systemctl", "disable", "systemd-resolved.service"])
    if result.returncode:
        return False
    result = subprocess.run(["systemctl", "stop", "systemd-resolved.service"])
    if result.returncode:
        return False
    return True

def enableIPForward():
    result = subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=1"])
    if result.returncode:
        return False
    return True

def disableIPForward():
    result = subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=0"])
    if result.returncode:
        return False
    return True

#
# Description: ALlows to kill all aircrack-ng process
# Return: True if succeded else False
#
def killall():
    processKIll = subprocess.run(["kilall", "airbase-ng", "airmon-ng", "dnsmasq"])
    if not processKIll.returncode:
        return False
    return True


def launchDnsmasq(path):
    result = subprocess.Popen(["dnsmasq", "-C", path])
    if result.returncode:
        return False
    return True

def launchDnsSpoof():
    result = subprocess.Popen(["dnsspoof", "-i", "at0"])

def stopSytemdResolve():
    result = subprocess.run(["killall", "systemd-resolve"])

def addRoute():
    result = subprocess.run(["route", "add", "-net", "10.0.0.0", "netmask", "255.255.255.0", "gw", "10.0.0.1"])

def iptableSet():
    subprocess.run
clear = lambda: os.system('clear')