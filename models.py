
#
# Description: Represent one hotspot
#
class hotspot:
    ssid = ""
    channel = ""
    address = ""
    quality = ""

    def __init__(self, ssid, channel, address, quality):
        self.ssid = ssid
        self.channel = channel
        self.address = address
        self.quality = quality

    def __str__(self):
        result = "SSID: {} - Channel: {} - Address: {} - Quality: {}".format(self.ssid, self.channel, self.address, self.quality)
        return result

    def getName(self):
        return self.ssid
