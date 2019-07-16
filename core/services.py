import subprocess

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