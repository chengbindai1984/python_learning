#! /usr/bin/env python3

Passwords = {'email': "!QAZ2wsx", 'blog': "!@#$qwer", 'luggage': "ERDFAF"}

import sys
import pyperclip

if len(sys.argv) < 2:
    print ("Usage: py pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in Passwords:
    pyperclip.copy(Passwords[account])
    print ('Password for ' + account + ' copied to clipboard.')
else:
    print ('There is no account named ' + account)
