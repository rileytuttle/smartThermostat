#!/usr/bin/python
#thermostat on
import RPi.GPIO as GPIO
import Adafruit_DHT
thermostatPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(thermostatPin, GPIO.OUT)
tempPin = 27
sensor = 22
class thermostat():
	@staticmethod
	def getTemp():
		#probably more difficult than this
		humidity, temperature = Adafruit_DHT(sensor, tempPin)
		return temperature
	@staticmethod
	def setTemp(desiredTemp):
		curTemp = getTemp()
		if desiredTemp > curTemp:
			GPIO.output(thermostatPin, GPIO.HIGH)
		else:
			GPIO.output(thermostatPin, GPIO.LOW)
		return

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
