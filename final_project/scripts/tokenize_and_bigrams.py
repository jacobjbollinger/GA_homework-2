from time import sleep
import os
import re
import collections

from nltk.corpus import stopwords

from nltk.tokenize import regexp_tokenize

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

punctuation = re.compile(r'[-.?!%,";:()|0-9]')

for a in range(2013,2014):

	sleep(1)
	print "\n...starting %s files" % str(a)

	directory = "../data/text/%s" % str(a)
	files = os.listdir(directory)

	for f in files:

		if ".txt" in f:
			try:

				filename = directory + "/" + f
				
				# === Word list and stopwords ===

				word_list = re.split('\s+', open(filename).read().decode('utf-8-sig').lower())
				words = (punctuation.sub("", word).strip() for word in word_list)
				words = (word for word in words if word not in stopwords.words('english'))

				# === Bigrams ===
				
				bcf = BigramCollocationFinder.from_words(words)
				print bcf.nbest(BigramAssocMeasures.likelihood_ratio, 10)

"""				# === Trigrams ===

				tcf = TrigramCollocationFinder.from_words(words)
				print tcf.nbest(TrigramAssocMeasures.likelihood_ratio, 10)
"""				
			except: 
				pass
