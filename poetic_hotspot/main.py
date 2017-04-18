from network import WLAN
import time
import pycom

pycom.heartbeat(False)
limerik = '''Hickory, dickory, dock!
The mouse ran up the clock.
The clock struck one –
The mouse ran down.
Hickory, dickory, dock!'''
wlan = WLAN()

while(1):
    for i in limerik.split('\n'):
        pycom.rgbled(0x007f00)
        wlan.ssid(i)
        time.sleep(.3)
        pycom.rgbled(0x000000)
        time.sleep(10)
