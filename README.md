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
If it's not working, it might be that you are not using the "pi" user. If so, refer to the "Use a different user" section bellow.  
If that's not the issue, refer to the "troubleshooting" section.  

## Run at startup
By default, the service is configured to run at startup.  
Here's how to enable or disable the service:  
Make it run at startup: `sudo systemctl enable qmk_irpi`  
Make it not run at startup: `sudo systemctl disable qmk_irpi`  

## Hardware installation
Check out [this documentation](https://github.com/hQamonky/IRRemotePi/tree/master/docs/Hardware%20Installation.md).

# Updates
Updates work the same as installation but with the [update.sh](https://raw.githubusercontent.com/hQamonky/IRRemotePi/master/update.sh) script or the [update_force.sh](https://raw.githubusercontent.com/hQamonky/IRRemotePi/master/update_force.sh) script.  

## Safe update
The "normal" update will not work if some changes have been done to the structure of the database. But if it works you will maintain all the remotes and IR commands that you registered and recorded.  
Open a terminal and run:   
> `~/qmk/IRRemotePi/update.sh`  

## Hard update
The "hard" update **will overwrite your database**, meaning that you will **lose all the remotes and IR commands that you registered and recorded**.  
But it is required if you want to update and if the "normal" update doesn't work.  
Open a terminal and run:  
> `~/qmk/IRRemotePi/update_force.sh`  

# Usage
The install.sh script installs the service as a systemd service. So you can manage it using the following commands:  
> `sudo systemctl start qmk_irpi`    
> `sudo systemctl stop qmk_irpi`    
> `sudo systemctl restart qmk_irpi`  
    
The documentation for using the API is accessible [here](https://github.com/hQamonky/IRRemotePi/blob/master/docs/API%20User%20Guide.md), at the `/` endpoint of the API, or directly in your installation folder at `~/qmk/IRRemotePi/docs/API\ User\ Guide.md`.  

## Use a different port
By default, the API is accessible on the 8094 port. If you want to change this, edit the run.py file and change the 8094 value to whatever port you want.  

# Troubleshooting
The service is installed as a systemd service by default. This means you can see logs and stuff by using the `journalctl` command.  
Check online for more information about `systemd`, `systemctl` and `journalctl`.  

## Use a different user
If you are not using the default user on your raspberry (which is called "pi"), the default configuration won't work. But you can fix it like so:  
Edit the qmk_irpi.service file:   
`sudo nano /etc/systemd/system/qmk_irpi.service`  
Then, replace `pi` with your own username.  
```
. . . 

User=<your_username>
WorkingDirectory=/home/<your_username>/qmk/IRRemotePi
ExecStart=/home/<your_username>/qmk/IRRemotePi/run.sh

. . . 
```
