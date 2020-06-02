#!/bin/bash

git -C ~/qmk/IRRemotePi pull
# Restart service
sudo systemctl restart qmk_irpi