#! /usr/bin/python3
# lucky.py - Opens several Google search results

import sys, webbrowser, bs4, requests

# downloading the page
print('Googling .......')
searchTerm = ' '.join(sys.argv[1:])
res = requests.get('http://google.com/search?q=' + searchTerm)
res.raise_for_status

# get the top links through bs4
soup = bs4.BeautifulSoup(res.text,'lxml')
linkElems = soup.select('.r a')

# open those links in browser
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get('href'))
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
