#!/bin/sh

# This is used for testing the tool on a Raspberry Pi (RPi).

# A single argument is required that is the RPi IP address.
HOST=$1

#The folder to scp the installer files into. This must be manually created on the RPi before use.
TARGET_FOLDER=/home/pi/pip/smotor

# Copy the files to the RPi
scp -r smotor scripts install.sh uninstall.sh setup.py README.md pi@$HOST:$TARGET_FOLDER

#Once copied the install script can be executed to install the smotor module onto the RPi
# Note that the Rpi must have at least python3.8 installed (executed when python3 is entered).