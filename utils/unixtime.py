#!/bin/python3

import time
import os

#one liner install
#sudo curl "https://raw.githubusercontent.com/ozzyisgreat/miscellaneous/main/utils/unixtime.py" -o /bin/unixtime; sudo chmod +x /bin/unixtime; echo Done! type "unixtime" to run

while True:
        t = str(time.time())
        t = t.split(".", 1)[0]
        time.sleep(1)
        os.system("clear")
        print(t)
