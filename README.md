PunyDDNS Updater
================

A simple Python script to update your PunyDDNS. It was made to work on the Raspberry Pi.

## PunyDDNS

You can find out more about Puny at [sl.pt](http://sl.pt).

## Dependencies

It uses the requests lib from Kenneth Reitz:

[https://github.com/kennethreitz/requests](https://github.com/kennethreitz/requests)

## Instalation

First edit the script and change the ```domain```, ```username``` and ```password``` variables at the top.
Copy the script to ```/usr/local/bin``` and edit your ```/etc/network/interfaces``` file:

Before

```
...
iface eth0 inet dhcp
...
```

After 

```
...
iface eth0 inet dhcp
	up python /usr/local/bin/updatePunyDDNS.py
...
```