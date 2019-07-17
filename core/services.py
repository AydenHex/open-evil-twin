import subprocess
import sys

from core.utils import FNULL


def killProcess(interface):
    subprocess.run(["killall", "dnsmasq"])

def launchDnsmasq(path):
    result = subprocess.Popen(["dnsmasq", "-C", path], stdout=FNULL)
    if result.returncode:
        return False
    return True

def launchDnsSpoof():
    result = subprocess.run(["dnsspoof", "-i", "at0"], stdout=FNULL, stderr=subprocess.STDOUT)

def stopSystemdResolved():
    result = subprocess.run(["systemctl", "disable", "systemd-resolved.service"], stdout=FNULL)
    if result.returncode:
        sys.exit("Error, can't stop systemd-resolved")
    result = subprocess.run(["systemctl", "stop", "systemd-resolved.service"])
    if result.returncode:
        sys.exit("Error, can't stop systemd-resolved")

def startSystemdResolved():
    result = subprocess.run(["systemctl", "enable", "systemd-resolved.service"], stdout=FNULL)
    if result.returncode:
        sys.exit("Error, can't stop systemd-resolved")
    result = subprocess.run(["systemctl", "start", "systemd-resolved.service"], stdout=FNULL)
    if result.returncode:
        sys.exit("Error, can't stop systemd-resolved")

def iptablesSet():
    subprocess.run(["iptables", "--append", "FORWARD", "--in-interface", "at0", "-j", "ACCEPT"], stdout=FNULL)
    subprocess.run(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--dport", "80", "-j", "DNAT", "--to-destination", "10.0.0.1:80 "], stdout=FNULL)
    subprocess.run(["iptables", "-t", "nat", "-A", "POSTROUTING", "-j", "MASQUERADE"], stdout=FNULL)

def iptablesDel():
    subprocess.run(["iptables", "-D", "FORWARD", "--in-interface", "at0", "-j", "ACCEPT"])
    subprocess.run(["iptables", "-t", "nat", "-D", "PREROUTING", "-p", "tcp", "--dport", "80", "-j", "DNAT", "--to-destination", "10.0.0.1:80 "], stdout=FNULL)
    subprocess.run(["iptables", "-t", "nat", "-D", "POSTROUTING", "-j", "MASQUERADE"], stdout=FNULL)
