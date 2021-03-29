#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns")
protoa.append("dns")
print(proto)
proto2 = [ 22, 80, 443, 53 ]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)
