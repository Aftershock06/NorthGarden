# This repo is for a homebased webserver to monitor a small garden
> Just using this space to keep notes of the work that is happening; 


- [Step 1](#step1)
- [Step 2](#step2)
- [Step 3](#step3)
- [Step 4](#step4)
- [Step 5](#step5)
- [Step 6](#step6)


## Example

## Steps/Process: 

### Step. 1 Create new SD Card for Pi  <a name="step1"></a>
Install Raspbian Lite on an SD Card and Installing on Raspberry Pi Zero 

### Step. 2 Maintain IP Address <a name="step2"></a>
Updated the domain files so the IP address stays the same no matter what. [Guide](https://github.com/Aftershock06/NorthGarden/blob/master/ipAddressSteps.md)

### Step. 3 Install Git <a name="step3"></a>

SSHing in to the Pi and updating it and install git 

```
sudo apt upgrade 
sudo apt list --upgradeable 
``` 
> upgrades all available sources 
```
sudo apt install git 
```

### Step. 4 Install Apache <a name="step4"></a>

```
sudo apt install apache2 -y
sudo service apache2 status
```

### Step. 5 Clone this Git <a name="step5"></a>

Cloning the git repo into the var/www/html files

### Step. 6 Setup Enviro-Grow <a name="step6"></a>

Setting up the enviro grow to add data to a new file envirogrow.csv
 

