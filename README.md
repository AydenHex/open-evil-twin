
# [WIT] Open Evil Twin (OET)

Open Evil Twin is a tool developed in python3. Designed for pentesters, it simplifies *Evil Twin* attacks and, in the future, the gathering of stolen credentials.

It is based on **aircrack-ng** to create the hotspot, **Dnsmasq** to manage dhcp and dns service, and **Dnsspoof** (Dsniif) to redirect the user to the fake proxy page.

/!\ **The current version doesn't redirect to the internet** /!\

## Motivations

Open Evil Twin's main objective is to offer pentesters a complete tool allowing them to simulate Evil Twin attacks more easily, thus allowing companies to become aware that CyberSecurity training (both regarding risk awareness, but also important security practices) is a necessity today.

## Features

**Evil Twin Attack**: OET allows to launch an Evl Twin attack with any web server as Apache or Nginx because we doesn't manage in the current version this part of Evil Twin Attack. However you can configure dns and dhcp as you wish.

**Wifi Scanning**: OET can scan nearby wifi hotspot and gives you an overview of possible targets.

**Environment Checking**: OET checks if its environment has all the needed packages to work correctly.

## Installation and Usage

First, clone the repository:

```bash
git clone https://github.com/AydenHex/open-evil-twin.git
```
You can then launch OET with this command: 
```bash
cd open-evil-twin/
pip3 install -r requirements.txt
python3 open-evil-twin.py
```
Open Evil Twin checks if all dependencies are installed and gives you an overview of missing dependencies. 

OET will guide you through several menus.

## Features in development
* Unit Tests
* Services verification
* CI/CD Infrastructure
* Redirection to the internet
* Create and manage a web server
* And more...

## Contributors
* John Doe (co-founder)
