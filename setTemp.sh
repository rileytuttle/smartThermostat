#!/bin/bash
cd /home/pi/smartThermostat
python -c'from thermostatFunctions import setTemp; setTemp('$1')';
ticID=`python -c'from thermostatController import getTic; tic=getTic();print(tic)'`;
let "ticIDend= $ticID + 2 ";
./makeSchedule.sh $ticID $ticIDend $1
echo "3" > skipTicksLeft.txt
