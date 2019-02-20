#!/usr/bin/python3

import sniff

interface=input('What interface are you using? ')

sniff.all_traffic(interface)
