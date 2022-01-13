import os

e = input("whats the path to your file that you would like to purge: ")

print("Purging... (should take ~10 seconds)")
os.system(f"dd if=/dev/urandom of={e} & sleep 10 ; kill $!")
os.system(f"rm {e}")
print(f"{e} successfully purged")

#due to the dd and rm tool only being available in linux based distros this wont work on windows
