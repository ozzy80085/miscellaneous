import os
import sys

def purge(file):
	e = file

	#file content purge
	print("Purging... (pass 1/4)")
	os.system(f"dd if=/dev/zero of={e} & sleep 5; kill $!")
	print("Purging... (pass 2/4)")
	os.system(f"dd if=/dev/zero of={e} & sleep 5; kill $!")
	print("Purging... (pass 3/4)")
	os.system(f"dd if=/dev/zero of={e} & sleep 5; kill $!")
	print("Purging... (pass 4/4)")
	os.system(f"dd if=/dev/zero of={e} & sleep 5; kill $!")
	print("File contents successfully purged")

	#filename purge
	print("Purging filename...")
	os.system(f"mv {e} /tmp/0000")
	os.system(f"mv /tmp/0000 /tmp/000")
	os.system(f"mv /tmp/000 /tmp/00")
	os.system(f"mv /tmp/00 /tmp/0")
	print("Filename successfully purged")

	#Removing the file
	os.system(f"rm /tmp/0")
	print(f"{e} successfully purged")


menu = """
[1] Encrypt AES
[2] Decrypt AES
[3] File Purge
[99] Exit
"""

print(menu)
choice = input("your choice> ")


if choice == "1":
	os.system("clear")
	infile = input("what file would you like to encrypt: ")
	outfile = input("what would you like to call the encrypted file: ")
	password = input("what password would you like to encrypt the file with: ")
	os.system(f"openssl enc -aes-256-cbc -in {infile} -base64 -pbkdf2 -out {outfile} -pass pass:{password}")
	print(f"{infile} successfully encrypted")

if choice == "2":
	os.system("clear")
	decinfile = input("what file would you like to decrypt: ")
	decoutfile = input("what would you like the decrypted file to be called: ")
	password = input("what password would you like to decrypt the file with: ")
	os.system(f"openssl aes-256-cbc -d -in {decinfile} -base64 -pbkdf2 -out {decoutfile} -pass pass:{password}")
	os.system("clear")
	print(f"{decinfile} successfully decrypted")

if choice == "3":
	os.system("clear")
	delfile = input("what file do you want to purge: ")
	purge(delfile)

if choice == "99":
	print("hasta la vista, baby!")
	sys.exit()
