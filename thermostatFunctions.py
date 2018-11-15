#!/usr/bin/python
#thermostat on
import RPi.GPIO as GPIO
import Adafruit_DHT
thermostatPin = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(thermostatPin, GPIO.OUT)
tempPin = 27
sensor = 22
def getTemp():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, tempPin)
	return temperature
def getHum():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, tempPin)
	return humidity
def getState():
	state = GPIO.input(thermostatPin)
	#print(state)
	return state
def setState(state):
	GPIO.output(thermostatPin, state)
	return
def setTemp(desiredTemp):
	curTemp = getTemp()
	if desiredTemp > curTemp:
		GPIO.output(thermostatPin, GPIO.HIGH)
	else:
		GPIO.output(thermostatPin, GPIO.LOW)
	return
