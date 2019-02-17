#!/usr/bin/python3
import subprocess
import time
interface=input('What interface are you using')
p=subprocess.Popen(['airodump-ng', interface])
time.sleep(6)
subprocess.call(['killall', 'airodump-ng'])


