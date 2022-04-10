#!/bin/python3
import subprocess

cmd = ["id" " | " "awk " "\'{print $1}\'"]

comm = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

comm = comm.stdout.decode("utf-8")

for char in "()=abcdefghijklmnopqrstuvwxyz\n":
                comm = comm.replace(char, '')
if comm != "0":
        print("your not root")

else:
        print("your root")
