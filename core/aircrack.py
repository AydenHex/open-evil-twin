import subprocess

#
# Description: Allows to put an wifi module in monitor mode
# Param: the interface of wifi module
# Return: True if process succeded, else false
#
def airmonStart(interface):
    processAirmon = subprocess.call(["airmon-ng", "start", interface])
    if not processAirmon:
        return True
    return False


#
# Description: Allows to put an wifi module in monitor mode
# Param: the interface of wifi module
# Return: True if process succeded, else false
#
def airmonStop(interface):
    processAirmonStop = subprocess.call(["airmon-ng", "stop", interface])
    if not processAirmonStop:
        return True
    return False


#
# Description: Allow to launch an evil twin attack
# Param: the interface of wifi module
# Param: the ssid of the target
# Param: the channel of the target
#
def airbaseStart(interface, ssid, channel):
    processAirbaise = subprocess.Popen(["airbase-ng", "-e", "rootsh3ll", "-c", channel, interface, "-q"])
    if not processAirbaise:
        return False, processAirbaise
    return True, None