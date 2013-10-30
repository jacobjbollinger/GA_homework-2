from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from time import sleep
import csv

for a in range(2005,2013):
    # create a directory "data/a"
    url = "http://cs229.stanford.edu/projects" + str(a) + ".html"
    # visit page
    # download each PDF on page 
    # save each PDF in directory
    print url



soup = bs(urlopen(url).read())

