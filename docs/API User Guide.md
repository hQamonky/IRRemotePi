# IR Remote Pi

This document describes the endpoints of the IR Remote Pi API.  
IR Remote Pi ispython web API that enables you to record and send IR signals with a Raspberry Pi.    

**Vocabulary**  
- Devices  
Basically represents an IR remote control. It will have a name and a list of commands.  
- Commands  
Basically represents a button of an IR remote control. It will have a name and a signal, and it will be part of a device.  

# Endpoints

- `/` - access API documentation (this document)
- `/database/clear` - create or restore database  
- `/devices` - manage devices  
- `/device/<device_id>` - manage devices  
- `/device/<device_id>/record` - record IR signals to create commands  
- `/device/<device_id>/command/<command_id>` - manage commands  
- `/device/<device_id>/send/<command_id>` - send an IR signal  

## Access API documentation

`GET` `/`  
  
Returns this document as html format.  

## Create or restore database

`GET` `/database/clear`  
  
Clears the entire database.  
Creates the database if it doesn't exist.  

## List devices

`GET` `/devices`
  
Returns the list of devices as json format.  
Does not return the commands of each device.    
***Response Example***  
```json
{
    "message": "Success",
    "data": [
        {
            "id": 1,
            "name": "Logitech Z906"
        },
        {
            "id": 2,
            "name": "HDMI Switch"
        }
    ]
}
```

## Create a new device

`POST` `/devices`

Create a new device. Takes json as body format.  
  
***Body Example***  
```json
{
	"name": "Logitech Z906"
}
```

## Get specific device

`GET` `/device/<device_id>`  
  
Returns specified device as json format. Also returns the list of commands of the device.  
  
***Response Example***  
```json
{
    "message": "Success",
    "data": {
        "name": "HDMI Switch",
        "commands": [
            {
                "id": 4,
                "device_id": 1,
                "name": "on/off",
                "signal": "test signal"
            },
            {
                "id": 5,
                "device_id": 1,
                "name": "Audio",
                "signal": "test signal"
            }
        ]
    }
}
```

## Edit a specific device

`POST` `/device/<device_id>`  
  
Edit the specified device. Takes json as body format.  
  
***Body Example***  
```json
{
	"name": "Logitech Z906 THX"
}
```

## Delete a specific device

`DELETE` `/device/<device_id>`  
  
Delete the specified device.  

## Record an IR signal

`POST` `/device/<device_id>/record`
  
Triggers the raspberry to start recording IR signals from its IR receiver.  
You have to record the signal while this page is loading: it will not load as long as it does not receive an IR signal. So press on the button that you want to record to make it load.  
Specify the id of the device for which you want to save the command in the URL.  
Set other parameters in the request body with json as body format.  
  
***Body Example***  
```json
{
	"command_name": "on/off"
}
```

## Edit a specific command

`POST` `/device/<device_id>/command/<command_id>`
  
Edit a command name. Takes a body as json format.  
You cannot edit a command's signal. You have to delete the command and re-create (re-record) it in order to do that.  
  
***Body Example***  
```json
{
	"command_name": "On / Off"
}
```

## Delete a specific command

`DELETE` `/device/<device_id>/command/<command_id>`  
  
Delete the specified command.  
  
## Send an IR signal

`GET` `/device/<device_id>/send/<command_id>`
  
Send the IR signal of the specified command from the specified device.  
