#!/usr/bin/env python3

import uuid

howmany = int(input("How many UUIDs should be generated? "))

for random in range(howmany):
    print( uuid.uuid4() )
