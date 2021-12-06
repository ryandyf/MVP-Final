#!/usr/bin/env python3
# Import scapy
from scapy.all import *
from scapy.layers.l2 import ARP, arping
import sys
import os
from scapy.layers.l2 import Ether
# We need to create regular expressions to ensure that the input is correctly formatted.
import re

def start():
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    if os.path.exists("ip.txt"):
        runScapy()
    else:
        while True:
            #A loop that asks for a valid IP address until one is given in format x.x.x.x/x
            ip_add_range_entered = input(
                "\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
            #Converts the user's input into regular expression so the program can understand what is being written
            if ip_add_range_pattern.search(ip_add_range_entered):
                print(f"{ip_add_range_entered} is a valid ip address range")
                #Writes down the IP Address so the function repeat() will be used when this script is executed again
                writeIP = open("ip.txt", "w")
                writeIP.write(ip_add_range_entered)
                print("Wrote IP down for future use...")
                writeIP.close()
                break
        runScapy()
    # Try ARPing the ip address range supplied by the user.
    # The arping() method in scapy creates a packet with an ARP message
    # and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
    # If a valid ip address range was supplied the program will return
    # the list of all results.
def runScapy():
    regcompile = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    ip = open("ip.txt", "r")
    ip = ip.readlines()[0]
    regcompile.search(ip)
    if os.path.exists("MASTER.json"):
        print("Created REPEAT.txt")
        sys.stdout = open('REPEAT.txt', 'wt')
    else:
        print("Created MASTER.txt")
        sys.stdout = open('MASTER.txt', 'wt')
    arp_result = arping(ip)
start()