import serial

ser = serial.Serial('/dev/ttyAcm0', 9600)

while True:
	print(ser.readline())