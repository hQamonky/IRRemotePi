#!/bin/bash

# Update
git -C ~/qmk/IRRemotePi pull
# Set permissions
chmod +x ~/qmk/IRRemotePi/run.sh
chmod +x ~/qmk/IRRemotePi/update.sh
chmod +x ~/qmk/IRRemotePi/update_force.sh
# Restart service
sudo systemctl restart qmk_irpi