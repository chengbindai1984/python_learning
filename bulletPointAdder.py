#! /usr/bin/env python3

# desribe your purpose here

import pyperclip

text = pyperclip.paste()

#ToDo: Seperage lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+ lines[i]

text ='\n'.join(lines)

pyperclip.copy(text)