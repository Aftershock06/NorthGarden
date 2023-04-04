# This repo is for a homebased webserver to monitor a small garden
> Just using this space to keep notes of the work that is happening; 

## Steps/Process: 

### Step. 1 Create new SD Card for Pi  
Install Raspbian Lite on an SD Card and Installing on Raspberry Pi Zero 

### Step. 2 Maintain IP Address
Updated the domain files so the IP address stays the same no matter what. [Guide](https://github.com/Aftershock06/NorthGarden/blob/master/ipAddressSteps.md)

### Step. 3 Install Git 

SSHing in to the Pi and updating it and install git 

```
sudo apt upgrade 
sudo apt list --upgradeable 
``` 
> upgrades all available sources 
```
sudo apt install git 
```

### Step. 4 Install Apache

```
sudo apt install apache2 -y
sudo service apache2 status
```

### Step. 5 Clone this Git 

Cloning the git repo into the var/www/html files

### Step. 6 Setup Enviro-Grow 

Setting up the enviro grow to add data to a new file envirogrow.csv
 
<details>
  <summary>Test</summary> 
   This is a test to see how things work. 

</details>
