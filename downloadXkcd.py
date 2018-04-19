#! /usr/bin/python3
# downloadXkcd.py - downloads all XKCD comics

import os, bs4, requests

url = 'http://xkcd.com'   # starting url
os.makedirs('xkcd', exist_ok = True)  # store comics in ./xkcd folder

while not url.endswith('#'):
    # download the page
    print('downloading the page %s' % (url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")
    # find the url of the image
    comicElem = soup.select('#comic img')
    if comicElem == [] :
        print('could not find the image')
    else :
        comicUrl = 'http:' + comicElem[0].get('src')
        # download the image
        print('downloading the image %s' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status
        # save the image to ./xkcd
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # find the previous button url
    previousLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + previousLink.get('href')

print('Done')
