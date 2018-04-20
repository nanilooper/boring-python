#! /usr/bin/python3
# multidownloadXkcd.py - Download xkcd comics using mutiple threads

import requests, bs4, os, threading
os.chdir('../')
os.makedirs('./xkcd', exist_ok = True) # store comics in ../xkcd

# function to download xkcd comics in a given range
def downloadXkcd(startComic, endComic):
    for urlNum in range(startComic, endComic):
        # download the page
        res = requests.get('http://xkcd.com/%s' % (urlNum))
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

# create and start the thread objects
downloadThreads = [] # a list to track all the download threads
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args = (i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# wait for all threads to complete
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done')
