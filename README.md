# IRRemotePi
IR Remote Pi is a python web API that enables you to record and send IR signals with a Raspberry Pi.  
This has been tested on a Raspberry Pi 2 model B v2 with Raspbian Buster (release 10), but it should work on any Raspberry Pi.  

# Installation   
You can use the [install.sh](https://raw.githubusercontent.com/hQamonky/IRRemotePi/master/install.sh) script to install automatically, or you can check out the commands in the [install.sh](https://raw.githubusercontent.com/hQamonky/IRRemotePi/master/install.sh) script and run them manually.  

## Automatic installation
Open a terminal and run:  
> `wget -P ~/Downloads https://raw.githubusercontent.com/hQamonky/IRRemotePi/master/install.sh`  
> `chmod +x ~/Downloads/install.sh`  
> `~/Downloads/install.sh`  

When the installation script is finished, the service should be running.  
Verify by entering the ip address of your Raspberry Pi in the web browser on the port number 8094.   

## Run service at startup
Make the run script executable: `chmod +x ~/qmk/IRRemotePi/run.sh`  
Edit cron with `sudo crontab -e`  
Add the following line at the end of the file:  
`@reboot ~/qmk/IRRemotePi/run.sh &`  
Save and exit.  
Verify that is worked by trying to access the API after rebooting the Raspberry.  

## Hardware installation
Check out [this documentation](https://github.com/hQamonky/IRRemotePi/tree/master/docs/Hardware%20Installation.md).

# Updates
Updates work the same as installation but with the [update.sh](https://raw.githubusercontent.com/hQamonky/IRRemotePi/master/update.sh) script or the [update_force.sh](https://raw.githubusercontent.com/hQamonky/IRRemotePi/master/update_force.sh) script.  

## Safe update
The "normal" update will not work if some changes have been done to the structure of the database. But if it works you will maintain all the remotes and IR commands that you registered and recorded.  
Open a terminal and run:   
> `chmod +x ~/qmk/IRRemotePi/update.sh`  
> `~/qmk/IRRemotePi/update.sh`  

## Hard update
The "hard" update **will overwrite your database**, meaning that you will **lose all the remotes and IR commands that you registered and recorded**.  
But it is required if you want to update and if the "normal" update doesn't work.  
Open a terminal and run:  
> `chmod +x ~/qmk/IRRemotePi/update_force.sh`  
> `~/qmk/IRRemotePi/update_force.sh`  

# Usage
Check out the [run.sh](https://raw.githubusercontent.com/hQamonky/IRRemotePi/master/run.sh) script to see how to launch the service.  
The documentation for the API is accessible [here](https://github.com/hQamonky/IRRemotePi/blob/master/docs/API%20User%20Guide.md), at the `/` endpoint of the API, or directly in your installation folder at `~/qmk/IRRemotePi/docs/API\ User\ Guide.md`.  

## Use a different port
By default, the API is accessible on the 8094 port. If you want to change this, edit the run.py file and change the 8094 value to whatever port you want.  
