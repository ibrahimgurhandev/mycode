#!/usr/bin/env python3

hostname = input("what value should we set for hostname")

if hostname.lower() == "MTG":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
elif hostname == "":
    print("You didn't type anything in, dummy")
print("Exiting the script")