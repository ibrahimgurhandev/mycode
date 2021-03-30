#!/usr/bin/env python3
import ipaddress

ipchk = input("Apply an IP address: ")
IPvalidated = False

try:
    ipaddress.IPv4Network(ipchk)
    IPvalidated = True
except ValueError:
    IPvalidated = False

if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif IPvalidated:
   print("Looks like the IP address was set: " + ipchk)
else:
   print("You did not provide correct input or a correct IP.")