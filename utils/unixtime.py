#!/bin/python3

import time
import os


while True:
        t = str(time.time())
        t = t.split(".", 1)[0]
        time.sleep(1)
        os.system("clear")
        print(t)
