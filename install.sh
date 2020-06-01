#!/bin/bash

# Update your system
sudo apt update && sudo apt ugrade -y
# Install dependencies
sudo apt install python3-pip virtualenv git
sudo pip3 install --upgrade setuptools
# Create application environment
mkdir -p ~/qmk && cd ~/qmk || exit
git clone https://github.com/hQamonky/IRRemotePi.git
virtualenv IRRemotePi
cd IRRemotePi || exit
source bin/activate
pip3 install --no-cache -r ./requirements.txt
#sudo apt install libgpiod-dev # I'm not sure you need this
# Run service
python3 ./run.py