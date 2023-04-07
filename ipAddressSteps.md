# How to Set a Constant IpAddress

## Step 1 
To find the Raspberry Pi’s current IP address, enter the following command in a Terminal window:

```
hostname -I
```

• Your router’s gateway IP address – the one used to contact it from the local network, not its public IP. It varies depending on the router model, but typically starts with 192.168.

To find it, enter the following command and note the first IP address given:


```
ip r | grep default
```
Raspberry Pi router gateway IP
• Your router’s DNS (Domain Name System) IP address. This is typically the same as its gateway address, but may be set to another value to use an alternative DNS – such as 8.8.8.8 for Google, or 1.1.1.1 for Cloudflare.

To find the current DNS IP address, enter the command:
```
sudo nano /etc/resolv.conf
```
Raspberry Pi DNS IP
> Note the IP address after nameserver – that's the DNS address – and then press Ctrl + X to close the file.

## Step 2. Add Static IP Settings
Now you have found all your network connection information, it’s time to edit the dhcpcd.conf configuration file to add the settings you need to set up a static IP address for your Raspberry Pi:

```
sudo nano /etc/dhcpcd.conf
```
> Note: If you haven’t edited the file previously, it will mainly contain various comment lines preceded by a hash (#) symbol. At the bottom, add the following lines, replacing the emboldened names with your own network details:

interface <strong>NETWORK</strong> <br>
static ip_address=<strong>STATIC_IP</strong>/24 </br>
static routers=<strong>ROUTER_IP</strong> </br>
static domain_name_servers=<strong>DNS_IP</strong> </br> 
Replace the emboldened names as follows:

• NETWORK – your network connection type: eth0 (Ethernet) or wlan0 (wireless).

• STATIC_IP – the static IP address you want to set for the Raspberry Pi.

• ROUTER_IP – the gateway IP address for your router on the local network.

• DNS_IP – the DNS IP address (typically the same as your router’s gateway address).

Here is an example configuration to set the static IP to 192.168.1.120 with a wireless connection to a router at 192.168.1.254:

```
interface wlan0
static ip_address=192.168.1.120/24
static routers=192.168.1.254
static domain_name_servers=192.168.1.254
```
