import numpy
import pandas as pd
import os
import csv
from sklearn.feature_extraction import DictVectorizer

# change as appropriate
directory = os.getcwd()

## I couldn't find in sklearn where it found the attributes. It seemed like
## the feature vectors weren't about attributes and the topic modeling I have
## found earlier was hard to use so I decided to follow this tutorial:
## https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24

## I also only downloaded one data file because they were big so this code looks at all of the data files at once
## instead of each one individually so that also needs to be changed.

import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import nltk
nltk.download('wordnet')
stemmer = SnowballStemmer("english")

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


reviewlist = []
with open("data/Appliances.csv", newline='') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        review = row[5] ## reviewText is the 6th column
        reviewlist.append(review)

processed_reviews = []
for review in reviewlist:
    processed_reviews.append(preprocess(review))
dictionary = gensim.corpora.Dictionary(processed_reviews)
dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_reviews]

from gensim import corpora, models
tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

## One way to find attributes
lda_model = gensim.models.LdaModel(bow_corpus, num_topics=10, id2word=dictionary, passes=2)

# for idx, topic in lda_model.print_topics(-1):
#     print('Topic: {} \nWords: {}'.format(idx, topic))


## Second way to find attributes
lda_model_tfidf = gensim.models.LdaModel(corpus_tfidf, num_topics=10, id2word=dictionary, passes=2)
for idx, topic in lda_model_tfidf.print_topics(-1):
    print(idx)
    print(topic)
