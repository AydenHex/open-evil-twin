# Open Evil Twin - OET [WIP]

This python client allow to scan nearby hotspots, create an evil twin attack and steal credentials

## Requirements

* dbus
* libdbus-glib-1-dev
* libdbus-1-dev
* python-dbus
* aircrack-ng
* dnsmasq

Python package
* wifi

```bash
sudo apt install dbus libdbus-glib-1-dev libdbus-1-dev python-dbus aircrack-ng dnsmasq
```

## Usage

/!\ You need to have an short interface name /!\ You can rename it with :

```bash
ifconfig <interface> down
ip link <interface> name <new interface name>
```


To launch this script, you need to be in root

#### Examples:

To scan hotspots:
```bash
python3 main.py --scan <interface>
```


