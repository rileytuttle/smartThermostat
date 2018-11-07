#!/usr/bin/python
#thermostat on

import RPi.GPIO as GPIO
import Adafruit_DHT
thermostatPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(thermostatPin, GPIO.OUT)
tempSensor = Adafruit_DHT22
tempPin = 18


def getTemp():
    #probably more difficult than this
    humidity, temperature = Adafruit_DHT(tempSensor, tempPin)
    return temperature

def setTemp(desiredTemp):
    curTemp = getTemp()
    if desiredTemp > curTemp:
        GPIO.output(thermostatPin, GPIO.HIGH)
    else
        GPIO.output(thermostatPin, GPIO.LOW)
    return
