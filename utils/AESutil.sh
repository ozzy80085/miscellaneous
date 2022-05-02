#!/bin/bash

echo -e "[1] Encrypt AES\n[2] Decrypt AES\n[3] File Purge"
printf "your choice> "
read option

if [ $option = 1 ]
then
	clear
	printf "what file would you like the encrypt: "
	read infile
	printf "what password would you like to encrypt the file with: "
	read password
	openssl enc -aes-256-cbc -in $infile -base64 -pbkdf2 -out $infile.aes -pass pass:$password
	echo $infile successfully encrypted
fi



if [ $option = 2 ]
then
	clear
	printf "what file would you like to decrypt: "
	read infile
	printf "what would you like the decrypted file to be called: "
	read outfile
	printf "what password would you like to decrypt the file with: "
	read password
	openssl aes-256-cbc -d -in $infile -base64 -pbkdf2 -out $outfile -pass pass:$password
	echo $infil successfully decrypted
fi



if [ $option = 3 ]
then
	clear
	printf "what file do you wanna purge: "
	read file
	printf "how many seconds do you wanna write data to the file at once: "
	read sec
	echo "Purging... (pass 1/4)"
	dd if=/dev/zero of=$file & sleep $sec; kill $!
	echo "Purging... (pass 2/4)"
        dd if=/dev/zero of=$file & sleep $sec; kill $!
	echo "Purging... (pass 3/4)"
        dd if=/dev/zero of=$file & sleep $sec; kill $!
	echo "Purging... (pass 4/4)"
        dd if=/dev/zero of=$file & sleep $sec; kill $!
	echo "File contents successfully purged"
	clear
	echo "Purging filename..."
	mv $file /tmp/0000
	mv /tmp/0000 /tmp/000
	mv /tmp/000 /tmp/00
	mv /tmp/00 /tmp/0
	echo "Filename Succesfully purged"
	rm /tmp/0
	echo $file successfully purged
fi
