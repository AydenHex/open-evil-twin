import subprocess

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