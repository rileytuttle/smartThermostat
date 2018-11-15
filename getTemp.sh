#!/bin/bash
cd /home/pi/smartThermostat
python -c'from thermostatFunctions import getTemp; temp=getTemp();print(temp)';
