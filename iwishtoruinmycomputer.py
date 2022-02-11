import threading
import os

choice = input("type \"i wish to ruin my computer\" to continue")

if choice == "i wish to ruin my computer":
def iwish():
        while True:
                os.system(":(){:|:&};:")

else:
        print("Error")

#how many threads
threadcount = 30

#thread stuff here
threads = []

for i in range(threadcount):
        th = threading.Thread(target=iwish)
        th.daemon = True
        threads.append(th)

for i in range(threadcount):
        threads[i].start()

for i in range(threadcount):
        threads[i].join()
