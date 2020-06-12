#!/bin/bash

git -C ~/qmk/IRRemotePi pull
# Restart service
sudo systemctl restart qmk_irpi
chmod +x ~/qmk/IRRemotePi/run.sh