mkdir ~/keys

#export public keys
gpg --armor --export > ~/keys/publickey.txt

#export private keys
gpg --armor --export-secret-keys > ~/keys/privatekey.txt

clear

echo "done"
echo "you can find your keys in the ~/keys directory"
