
from __future__ import division
from __future__ import print_function


class DummySerial(object):
	"""
	A dummy interface to test with when not hooked up to real hardware. It does
	a decent job of mimicing the real thing.
	"""
	def __init__(self, port, printAll=False):
		self.port = port
		self.printAll = printAll
		print('WARNING: Using fake ServoSerial')

	# @staticmethod
	# def listSerialPorts():
	# 	return ServoSerial.listSerialPorts()

	def open(self):
		pass

	def setRTS(self):
		pass

	def sendPkt(self, **kwargs):
		# print('serial write >>', pkt)
		return self.read()

	def read(self, how_much=128):
		return [[0xFF, 0xFF, 0xFD, 0x00, 0x01, 0x04, 0x00, 0x55, 0x00, 0xA1, 0x0C], [0xFF, 0xFF, 0xFD, 0x00, 0x03, 0x04, 0x00, 0x55, 0x00, 0xA1, 0x0C]]

	# def read(self, how_much=128):
	# 	return [0xFF, 0xFF, 0xFD, 0x00, 0x01, 0x04, 0x00, 0x55, 0x00, 0xA1, 0x0C]

	def write(self, data):
		# if self.printAll:
		# print('serial write >>', data)
		return len(data)

	def close(self):
		pass

	def flushInput(self):
		pass
