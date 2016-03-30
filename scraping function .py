
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


# In[ ]:

#This function scrapes the title, meta, and firts h1 tag from a given URL 
def scraper(url) :
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(), from_encoding=response.info().getparam('charset'))
    h = soup.find_all('h1')
    for link in h:
        names = link.contents[0]
        fullLink = link.get('href')
        h = names
    t = soup.find_all('title')
    for link in t:
        names = link.contents[0]
        fullLink = link.get('href')
        t = names
    m = metatag =soup.findAll(attrs={"name":"description"})
    metatag[0].attrs['content']
    df = pd.DataFrame({ 'tag' : ('title','meta', 'h1'),
                    'text' : (t,metatag[0].attrs['content'], h)
                    })
    return

