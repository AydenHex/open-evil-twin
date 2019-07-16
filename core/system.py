import subprocess

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