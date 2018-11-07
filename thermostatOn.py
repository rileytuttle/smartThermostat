#!/usr/bin/python
#thermostat on

import RPi.GPIO as GPIO
thermostatPin = 17
tempPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(thermostatPin, GPIO.OUT)
GPIO.setup(tempPin, GPIO.IN)

def getTemp():
    return int(GPIO.input(tempPin))

def setTemp(desiredTemp):
    curTemp = getTemp()
    if desiredTemp > curTemp:
        GPIO.output(thermostatPin, GPIO.HIGH)
    else
        GPIO.output(thermostatPin, GPIO.LOW)
    return
