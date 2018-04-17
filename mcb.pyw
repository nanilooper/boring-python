#! /usr/bin/python3
# mcb.pyw saves and loads pieces of text to clipboard
# Usage : python3 mcb.pyw save <keyword> - saves clipboard to keyword
#         python3 mcb.pyw <keyword> - saves keyword to clipboard
#         python3 mcb.pyw list - saves list of keywords available to clipboard
#         python3 mcb.pyw delete <keyword> - delete the keyword
#         python3 mcb.pyw delete  - delete all keywords

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 :
    # save keyword
    if sys.argv[1].lower() == 'save':
         keyword = sys.argv[2]
         text = pyperclip.paste()
         mcbShelf[keyword] = text
    # delete keyword
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords
    if sys.argv[1] == 'list':
        keys = list(mcbShelf.keys())
        pyperclip.copy('\n'.join(keys))
    # delete all keywords
    elif sys.argv[1] == 'delete':
        mcbShelf.clear()
    # copy keyword content to clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
