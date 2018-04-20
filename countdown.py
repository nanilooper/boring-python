#! /usr/bin/python3
# countdown.py - a simple countdown program

import time, subprocess, os, sys

timeLeft = 60
if len(sys.argv) > 1:
    timeLeft = int(sys.argv[1])

print('start')
while timeLeft > 0:
    print(timeLeft)
    sys.stdout.flush()
    time.sleep(1)
    timeLeft -= 1

# at the end of time play some alarm
os.chdir('../')
file = open('hello.txt', 'w')
file.write('time completed')
file.close()
subprocess.Popen(['gedit', 'hello.txt'])
