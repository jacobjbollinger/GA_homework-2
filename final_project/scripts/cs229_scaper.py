from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from time import sleep
import csv

for a in range(2005,2013):
    url = "http://cs229.stanford.edu/projects" + str(a) + ".html"
    print url


soup = bs(urlopen(url).read())

