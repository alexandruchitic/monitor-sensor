#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import os
import time

def on():
    print ("Turning display on.") #print message
    os.system('/usr/bin/tvservice -o') #making sure the display is off
    time.sleep(1)
    os.system('/usr/bin/tvservice --preferred') #display turn on
    os.system('/bin/fbset -depth 8') #display fbset
    os.system('/bin/fbset -depth 16') #display fbset
    os.system('/bin/fbset -depth 32') #display fbset
    time.sleep(1) #wait 1s 
    print ("Display turned on.")
    os.system('/bin/fbset -g 1920 1080 1920 1080 32') #display fbset
    time.sleep(60) #wait 60 sec before turn off
