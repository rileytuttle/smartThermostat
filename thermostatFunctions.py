#!/usr/bin/python
#thermostat on
import RPi.GPIO as GPIO
import Adafruit_DHT
thermostatPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(thermostatPin, GPIO.OUT)
GPIO.setwarnings(False)
tempPin = 27
sensor = 22
def getTemp():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, tempPin)
	return temperature*1.8+32
def setTemp(desiredTemp):
	curTemp = getTemp()
	if desiredTemp > curTemp:
		GPIO.output(thermostatPin, GPIO.HIGH)
	else:
		GPIO.output(thermostatPin, GPIO.LOW)
	return
