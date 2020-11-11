#!/bin/bash

RED="\033[1;31m"
GREEN="\033[1;32m"
NOCOLOR="\033[0m"

echo

echo -e "step 1: ${GREEN}pre-configuring packages${NOCOLOR}"
sudo dpkg --configure -a 

echo

echo -e "step 2: ${GREEN}fix and attempt to correct a system with broken dependencies${NOCOLOR}"
sudo apt-get install -f -y

echo

echo -e "step 3: ${GREEN}update apt cache${NOCOLOR}"
sudo apt-get update -y

echo

echo -e "step 4: ${GREEN}upgrade packages${NOCOLOR}"
sudo apt-get upgrade -y

echo

echo -e "step 5: ${GREEN}distribution upgrade${NOCOLOR}"
sudo apt-get dist-upgrade -y

echo

echo -e "step 6: ${GREEN}remove unused packages${NOCOLOR}"
sudo apt-get --purge autoremove -y

echo

echo -e "step 7: ${GREEN}clean up${NOCOLOR}"
sudo apt-get autoclean -y

echo

echo -e "step 8: ${GREEN}install python and it's packages${NOCOLOR}"
sudo apt install python3-dev python3-pip python3-tk -y

echo

echo -e "step 9: ${GREEN}install the modules${NOCOLOR}"
pip3 install pyarmor requests

echo

echo -e "${GREEN}done!${NOCOLOR}"

echo
