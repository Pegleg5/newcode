#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.extend("dns") # this line will add d, n, s
print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
proto.append(proto2) # pass proto2 as an argument to the append method
print(proto)  
h ="proto.count(h)" # this should count the number of h's in the script

#print(f"This is how many h's appear in the list {proto.count}")
print(f"This is how many h's appear in the list {proto.count('h')}")


