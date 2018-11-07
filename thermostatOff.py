#thermostat off

import RPi.GPIO as GPIO
thermostatPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(thermostatPin, GPIO.OUT)
GPIO.output(thermostatPin, GPIO.LOW)
