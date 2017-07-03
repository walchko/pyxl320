#!/usr/bin/env python

##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

from pyxl320 import Packet
# from pyxl320 import DummySerial
from pyxl320 import ServoSerial
import argparse


def handleArgs():
	parser = argparse.ArgumentParser(description='Sets a servo to an angle')
	parser.add_argument('-i', '--id', help='servo id', type=int, default=1)
	parser.add_argument('port', help='serial port  or \'dummy\' for testing', type=str)
	parser.add_argument('angle', help='servo angle in degrees: 0.0 - 300.0', type=float)

	args = vars(parser.parse_args())
	return args


def main():
	args = handleArgs()

	ID = args['id']
	port = args['port']  # '/dev/tty.usbserial-A5004Flb'
	angle = args['angle']

	print('Setting servo[{}] to {:.2f} on port {}'.format(ID, angle, port))

	if port.lower() == 'dummy':
		serial = ServoSerial(port=port, fake=True)
	else:
		serial = ServoSerial(port=port)
	serial.open()

	pkt = Packet.makeServoPacket(ID, angle)  # move servo 1 to 158.6 degrees
	ans = serial.sendPkt(pkt)  # send packet to servo
	if ans:
		print('status: {}'.format(ans))


if __name__ == '__main__':
	main()
