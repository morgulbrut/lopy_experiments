from network import LoRa
import socket
import time
import binascii
from machine import Pin
import pycom

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)
button = Pin('P10',Pin.IN,  Pin.PULL_UP)

# create an OTAA authentication parameters
app_eui = binascii.unhexlify('70 B3 D5 7E F0 00 37 3E'.replace(' ',''))
app_key = binascii.unhexlify('43 A4 E8 73 5C FB 95 3C 84 AE D8 55 20 3E 32 97'.replace(' ',''))


# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
reconnect_cnt = 0
while not lora.has_joined():
    time.sleep(2.5)
    print(reconnect_cnt)
    reconnect_cnt += 1

pycom.heartbeat(False)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket non-blocking
s.setblocking(False)

while(1):
    if not button.value():
        # send some data

        pycom.rgbled(0x7F0000)
        s.send(bytes([0x01]))
        # get any data received...
        data = s.recv(64)
        print(data)
        time.sleep(1)
        pycom.rgbled(0x000000)
