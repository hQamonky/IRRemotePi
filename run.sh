#!/bin/bash

sudo pigpiod
cd ~/qmk/IRRemotePi || exit
source bin/activate
python3 ./run.py