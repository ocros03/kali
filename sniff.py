#!/usr/bin/python3

import subprocess
import time


def main():

	interface=input('What interface are you using?')

	all_traffic(interface)


def all_traffic(interface):


	subprocess.Popen(['airodump-ng', interface])

	time.sleep(6)

	subprocess.call(['killall', 'airodump-ng'])

	return


if __name__=='__main__':
	main()
