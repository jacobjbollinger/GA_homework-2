from nltk.tokenize import regexp_tokenize

data = #data
regexp_tokenize(data, "[\w']+")


# stopwords
from nltk.corpus import stopwords

english_stops = set(stopwords.words('english'))
[word for word in tokens if word not in english_stops]


# or find within dictionary
ml_dictionary = 
[word for word in data if word not in ml_dictionary]


# bigrams

from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords

words = [w.lower() for w in webtext.words('grail.txt')]
bcf = BigramCollocationFinder.from_words(words)

stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset
bcf.apply_word_filter(filter_stops)
bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)

