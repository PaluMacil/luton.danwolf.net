# Luton

This holds the source code for luton.danwolf.net. 
It is initially focused on local services and client apps
for interaction with home automation and Raspberry Pi
registration. Some parts of this might only run within a
firewall.

## Setup

### Database

```commandline
sudo adduser luton
sudo -u postgres createuser --interactive
sudo -u postgres createdb luton
```