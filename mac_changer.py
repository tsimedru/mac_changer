#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (chose, arguments) = parser.parse_args()
    if not chose.interface:
        parser.error("[X] Please specify an interface, use --help for more information")
    if not chose.new_mac:
        parser.error("[X] Please specify an new MAC address, use --help for more information")
    return chose


def mac_changer(interface, new_mac):
    print("[O] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
mac_changer(options.interface, options.new_mac)
