#!/bin/bash
cd /home/pi/smartThermostat
python -c'from thermostatFunctions import getHum; hum=getHum();print(hum)';
