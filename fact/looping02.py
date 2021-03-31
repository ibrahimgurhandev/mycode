#!/usr/bin/env python3

with open("dnsservers.txt", "r") as dnsfile:

    for svr in dnsfile:
        print(svr, end="")
