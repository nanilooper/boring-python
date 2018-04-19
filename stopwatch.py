#! /usr/bin/python3
# stopwatch.py - stopwatch program

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.\
Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        laptime = round((time.time() - lastTime), 2)
        totalTime = round((time.time() - startTime),2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, laptime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
 # Handle the Ctrl-C exception to keep its error message from displaying.
 print('\nDone.')
