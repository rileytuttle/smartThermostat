#!/bin/bash
cd /home/pi/smartThermostat
python -c'from thermostatFunctions import getState; state=getState(); print(state)';
