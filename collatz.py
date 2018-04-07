#! /usr/bin/python3
#smallest math mystery

def collatz(num):
    if num % 2 == 0:
        return int(num/2)
    else:
        return 3*num + 1

def printcollatz(num):
    if num == 1:
        print(1)
        return
    while True:
        print(num)
        num = collatz(num)
        if num == 1 : print(1);break

num = input('enter a number :')
try:
    num = int(num)
except ValueError:
    print('enter a valid num')

printcollatz(num)
