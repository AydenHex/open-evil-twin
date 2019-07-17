from subprocess import call, Popen, PIPE

from core.utils import FNULL

#
# Description: Allows to put an wifi module in monitor mode
# Param: the interface of wifi module
# Return: True if process succeded, else false
#
def airmonStart(interface):
    processAirmon = call(["airmon-ng", "start", interface], stdout=FNULL)
    if not processAirmon:
        return True
    return False


#
# Description: Allows to put an wifi module in monitor mode
# Param: the interface of wifi module
# Return: True if process succeded, else false
#
def airmonStop(interface):
    processAirmonStop = call(["airmon-ng", "stop", interface], stdout=FNULL)
    if not processAirmonStop:
        return True
    return False


#
# Description: Allow to launch an evil twin attack
# Param: the interface of wifi module
# Param: the ssid of the target
# Param: the channel of the target
#
def airbaseStart(interface, hotspot):
    processAirbaise = Popen(["airbase-ng", "-e", hotspot.ssid, "-c", str(hotspot.channel), interface+"mon"])
