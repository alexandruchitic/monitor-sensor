#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import os
import time

def off():
    #~/opt/vc/bin/tvservice -s #display status
    print("Turning off monitor")
    os.system('/usr/bin/tvservice -s') #display status
    os.system('/usr/bin/tvservice -o') #display off
