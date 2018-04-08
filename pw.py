#! /usr/bin/python3
# pw.py - simple password storage program

PASSWORDS = dict(facebook='password', gmail='password', insta='password')

import sys,pyperclip
if len(sys.argv)<2:
    print('tell me what password do you need')
    sys.exit()

account = sys.argv[1] #account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])   #copies password to clipboard
    print('password copied for :' + account)
else:
    print('password not available for :' + account)
