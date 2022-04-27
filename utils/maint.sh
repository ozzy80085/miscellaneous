#!/bin/bash
#simple script i use to update and clear logs

sudo apt -y update
sudo apt -y upgrade
sudo apt -y autoremove
sudo apt clean

cd /var/log
rm *.gz
rm *.1
cd apache2
rm *.gz
rm *.1
echo "" > access.log
echo "" > error.log
clear
cd ~
echo Cleared!
