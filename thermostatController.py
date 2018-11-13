#!/usr/bin/python
#have a main loop
#every loop we first read the last or first line of the schedule txt
#for the skipTicksLeft.
#if it is <= 0
#	figure out what time it is in the day
#	then we read the corresponding line of the schedule.txt
#	then we read the temperature
#	turn thermostat on or off depending on the results
#else
#	skipTicksLeft--
#	write skipTicksLeft to the corresponding line of the schedule.txt
#

import time
import datetime
from thermostatFunctions import *

TICSIZE = 20


def getTic():
	now = datetime.datetime.now()
	midnight = now.replace(hour=0,minute=0,second=0,microsecond=0)
	secsSince = (now-midnight).seconds
	ticID = int(secsSince/60/TICSIZE)
	return ticID	

while True:
    #read first line of schedule
    f=open("skipTicksLeft.txt", "r")
    skipsLeft=int(f.readline())
    f.close()
    if skipsLeft > 0 :
        skipsLeft-=1
        f=open("skipTicksLeft.txt","w")
        f.write(str(skipsLeft))
        f.close()
    else:
        #get time and convert to number of 5 minute intervals since midnight
        #now = datetime.datetime.now()
        #midnight = now.replace(hour=0,minute=0,second=0,microsecond=0)
        #secsSince = (now-midnight).seconds
        #ticID = int(secsSince/60/TICSIZE)
        ticID = getTic()
	f=open("schedule.txt","r")
        lineList=f.readlines()
        setTemp(int(lineList[ticID]))
    time.sleep(TICSIZE*60) #make function to sleep for (5*60 seconds) 5 minutes

