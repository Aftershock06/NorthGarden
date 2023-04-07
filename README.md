# This repo is for a homebased webserver to monitor a small garden
> Just using this space to keep notes of the work that is happening; 

## Steps
- [Create New SD Card](#step1)
- [Change IP Address](#step2)
- [Install Git](#step3)
- [Install Apache](#step4)
- [Clone this Git](#step5)
- [Setup Data inputs as Jsons](#step6)
- [References](#ref)


# Let's Get Started

### Step 1. Create new SD Card for Pi  <a name="step1"></a>
Install Raspbian Lite on an SD Card and Installing on Raspberry Pi Zero 

### Step 2. Maintain IP Address <a name="step2"></a>
Updated the domain files so the IP address stays the same no matter what. [Guide](https://github.com/Aftershock06/NorthGarden/blob/master/ipAddressSteps.md)

### Step 3. Install Git <a name="step3"></a>

SSHing in to the Pi and updating it and install git 

```
sudo apt upgrade 
sudo apt list --upgradeable 
``` 
> upgrades all available sources 
```
sudo apt install git 
```

### Step 4a. Install Apache <a name="step4"></a>

```
sudo apt install apache2 -y
sudo service apache2 status
```

### Step 4b. Setup Flask Webserver

1. Install Flask on your Pi via Terminal 

```
sudo apt-get install python3-flask
```

2. Create a new project folder

```
mkdir gardenPiWebServer

<<<<<<< HEAD
=======
```
>>>>>>> fbd02a8572a46dbffa9664d1a3ce5a4fb0f1e4d8

### Step 5. Clone this Git <a name="step5"></a>

Clone git into /gardenPiWebServer Directory

### Step 6. Setup Enviro-Grow <a name="step6"></a>

Setting up the enviro grow to add data to a new file envirogrow.csv
 

### References Documents <a name="ref"></a>

[Creating a Flask Server](https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d)
