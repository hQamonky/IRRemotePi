#!/bin/bash

appdir=~/qmk

# Update your system
sudo apt update && sudo apt -y ugrade
# Install dependencies
sudo apt install python3-pip virtualenv git
sudo pip3 install --upgrade setuptools
# Create application environment
mkdir -p $appdir
git -C $appdir clone https://github.com/hQamonky/IRRemotePi.git
virtualenv $appdir/IRRemotePi
cd $appdir/IRRemotePi || exit
source bin/activate
pip3 install --no-cache -r ./requirements.txt
deactivate
#sudo apt install libgpiod-dev # I think we don't need this but I'm not sure.
# Make run script executable
chmod +x $appdir/IRRemotePi/run.sh
# Make update scripts executable
chmod +x $appdir/IRRemotePi/update.sh
chmod +x $appdir/IRRemotePi/update_force.sh
# Create systemd service
sudo cp $appdir/IRRemotePi/irremotepi.service /etc/systemd/system/qmk_irpi.service
sudo systemctl daemon-reload
sudo systemctl enable qmk_irpi
sudo systemctl start qmk_irpi