# sync_devices

## This python project syncs a folder on two devices 

the project uses sockets, especially User Datagram Protocol to keep two devices on the same WLAN connected.

### Usage:
    - Clone the repo.
    
    - You can make a virtual environment though the project does not use external dependencies.
    
    - The folder 'device_a' should be in one device and 'device_b' in another.
    
    - Connect devices on same network. Set the IP address of device_a (containing server.py in the header of client.py)
    
    - Create a few random files in both the folders (the files to be synced)

    - Run the files server.py and client.py on the two devices using:
    
        `python server.py`  and `python client.py`
        
    - There is a sync operation performed at every 10 seconds automatically, which can also start by typing 'sync' on device_b's console.
    
### What happens during the sync:

- The files added/ edited in any of the Devices are added to the same folder in other device.

- After the sync operation files on both the devices specify from which device the changes are.

- The types of file to be synced can be appended to the list 'ext', for now it is ext=['.txt']

### It looks somethin likes this:

`data.txt:` (on device A)

> We are going good.

> I have enough ammunition.

`data.txt:` (on device B)

> Let's attack in East direction

> Call.

> Attack

### After sync data.txt (on both devices) looks like:

> A --> We are going good.

> A --> I have enough ammunition.

> B --> Let's attack in East direction

> B --> Call.

> B--> Attack


If a file exists only on one device then it is also created on the other device during sync.

Please contact for additional changes.
