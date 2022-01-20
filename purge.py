import os
import time

os.system("clear")
e = input("Whats the path to your file that you would like to purge: ")

#File content purge
os.system("clear")
print("Purging... (pass 1)")
os.system(f"dd if=/dev/zero of={e} & sleep 5; kill $!")
os.system("clear")
print("Purging... (pass 2)")
os.system(f"dd if=/dev/zero of={e} & sleep 5; kill $!")
os.system("clear")
print("Purging... (pass 3)")
os.system(f"dd if=/dev/zero of={e} & sleep 5; kill $!")
os.system("clear")
print("Purging... (pass 4)")
os.system(f"dd if=/dev/zero of={e} & sleep 5; kill $!")
os.system("clear")
print("File contents successfully purged")


#Filename purge
print("Purging filename...")
os.system(f"mv {e} /tmp/0000")
os.system(f"mv /tmp/0000 /tmp/000")
os.system(f"mv /tmp/000 /tmp/00") 
os.system(f"mv /tmp/00 /tmp/0")

#removing the file
os.system(f"rm /tmp/0")
print(f"{e} successfully purged")
