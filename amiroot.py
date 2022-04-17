#!/bin/python3
import os

if str(os.geteuid()) == "0":
        print("you're root")

else:
        print("you're not root")
