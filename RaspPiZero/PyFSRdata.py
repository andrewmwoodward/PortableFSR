# FSR data collection script that communicates with an arduino over usb serial and saves to txt files
#
# A.Woodward Sept 2016

import RPi.GPIO as GPIO
import time
import serial
import os

#initial delay to ensure arduino has started
time.sleep(5)

ser = serial.Serial('/dev/ttyUSB0', 9600)
shutdownbutton = 25
buttonPin = 18
startLED = 23
collectLED = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(shutdownButton, GPIO.IN)
GPIO.setup(startLED, GPIO.OUT)
GPIO.setup(collectLED, GPIO.OUT)


def data_collect_save():
	print("Getting number to save")
	f = open('startup.txt', 'r+')
	save_num = int(f.readline().strip())
	f.close()
	output_file_name = "DataCollection" + save_num + ".txt"
	save_num = save_num + 1
	f.open("startup.txt",'w')
	f.write(str(save_num))
	f.close()
	print("Closing iterator number file")
	print("Opening output file")
	f = open(output_file_name, "w")
	read_data = "Start"
	while not read_data == "End":
		read_data = ser.readline().strip()
		if read_data == "---":
			f.write("\n")
		else:
			f.write(read_data + "\t")
	f.close()
	print("Closing output file")
	
	
	
	

print("Entering main loop")
while True:
	if GPIO.input(buttonPin):
		print("Button pressed")
		GPIO.output(collectLED, True)
		data_collect_save()
		GPIO.output(collectLED, False)
	if GPIO.input(shutdownButton):
		time.sleep(1)
		#avoid accidental shutdown presses
		if GPIO.input(shutdownButton): break
	time.sleep(0.1)

GPIO.output(23, False)
GPIO.cleanup()

os.system("sudo shutdown -h now")
		