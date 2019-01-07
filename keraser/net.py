#!venv/bin/python

'''
Useful stuff for networking.
'''

from config import Config
import logging
logger = logging.getLogger(Config.APP_NAME)

from subprocess import call
import datetime
import os
import io
import netifaces

def get_default_iface_name_linux():
    '''
    get the default interface name as a string
    '''
    route = "/proc/net/route"
    with open(route) as f:
        for line in f.readlines():
            try:
                iface, dest, _, flags, _, _, _, _, _, _, _, =  line.strip().split()
                if dest != '00000000' or not int(flags, 16) & 2:
                    continue
                return iface
            except:
                continue


def get_iface_mac_address(ifname='eth0'):
    '''
    get the mac address from the interface passed as a parameter
    '''
    macaddr = netifaces.ifaddresses(ifname)[netifaces.AF_LINK][0].get('addr')
    return macaddr