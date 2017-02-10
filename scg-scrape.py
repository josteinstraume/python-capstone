import urllib, csv, numpy
from BeautifulSoup import *

url = raw_input('Enter URL to crawl: ')
if len(url) < 1:
	url = 'http://sales.starcitygames.com//deckdatabase/deckshow.php?&t%5BC1%5D=3&start_num=0&start_num=0&limit=limit'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print 'TAG:', tag
    print 'URL:', tag.get('href', None)
    print 'Contents:', tag.contents[0]
    print 'Attrs:', tag.attrs
