#!/bin/python3

#pipe some hex into it 
#printf "hello" | hex | ./hextodec.py

hex = input("")

hexarr = [hex[i:i+2] for i in range(0, len(hex), 2)]

for i in hexarr:
        print(int(i, 16), end=" ")

print()
