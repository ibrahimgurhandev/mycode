#!/usr/bin/env python3

with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        svr = svr.rstrip('\n')

        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n"
                        )
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
