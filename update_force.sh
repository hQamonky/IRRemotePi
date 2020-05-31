#!/bin/bash

# Erase modifications (your database will be overwritten)
git -C ~/qmk/IRRemotePi reset --hard
# Update
git -C ~/qmk/IRRemotePi pull