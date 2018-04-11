#! /usr/bin/python3

#program to extract phone and emails from text

import re,pyperclip

#get text from the clipboard
text = pyperclip.paste()

#regex for catching phone numbers
phoneRegex = re.compile(r'''(
               (\+?\d{2})?\s{,2}  #country_code
               ([987]\d{9})       #phonenum
               )''',re.VERBOSE)
numbers = []
for match in phoneRegex.findall(text):
    numbers.append(match[0]+match[1])

#regex for catching emails
emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+     #username
                        @                     #symbol
                        [a-zA-Z0-9._]+        #domain
                        (\.[a-zA-Z]{2,4})     #dot-something
                         )''',re.VERBOSE)
emails = []
for groups in emailRegex.findall(text):
    emails.append(groups[0])

if len(numbers)+len(emails)>0:
    #copy numbers and emails to clipboard
    pyperclip.copy('\n'.join(numbers+emails))
    print('numbers and emails copied to clipboard')
else:
    print('no numbers and emails found')
