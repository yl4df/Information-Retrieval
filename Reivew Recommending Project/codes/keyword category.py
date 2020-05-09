import en_core_web_sm
import numpy
import pandas as pd
import os
import csv
from sklearn.feature_extraction import DictVectorizer

# change as appropriate
directory = os.getcwd()

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
for file in os.listdir(directory):
    if file.endswith(".csv"):
        with open(directory + "\\" + file, newline='') as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                review = row[5] ## reviewText is the 6th column
                reviewlist.append(review)

processed_reviews = []
for review in reviewlist:
    processed_reviews.append(preprocess(review))


import spacy

nlp = en_core_web_sm.load()
topic_labels = [i for i in range(10)
]
topic_keywords = [
    "gardus  sorri  wait  husband  serious  musti  tell  bunch  sit  tear",
"conveni  project  catcher  littl  lose  felt  wouldn  nest  contrapt  space",
    "open  mask  leaf  resist  ensur  littl  filter  unfortun  definit  unit ",
"instruct  climb  attic  buck  save  duct  push  unscrew  feet  marvel",
"thank  element  great  project  conveni  catcher  speed  lose  clutch  gardus",
"great  good  washer  tube  lazi  clod  foot  angl  figur  plier",
"price  better  great  littl  project  conveni  catcher  month  quick  problem",
"cycl  long  auto  good  run  potenti  gallon  bucket  jean  adapt",
"speed  clutch  perfect  high  fast  water  replac  pipe  half  slow",
"line  glad  wad  get  help  buy  free  shop  tri  necessari"
]

import itertools
import numpy as np
# Use pipe to run this in parallel
topic_docs = list(nlp.pipe(topic_keywords,
  batch_size=10000,
  n_threads=3))
topic_vectors = np.array([doc.vector
  if doc.has_vector else spacy.vocab[0].vector
  for doc in topic_docs])
print(topic_labels[0])
print(topic_vectors[0])

keywords = reviewlist[1:]

keyword_docs = list(nlp.pipe(keywords,
  batch_size=10000,
  n_threads=3))
keyword_vectors = np.array([doc.vector
  if doc.has_vector else spacy.vocab[0].vector
  for doc in keyword_docs])
print(keywords[0])
print(keyword_vectors[0])

from sklearn.metrics.pairwise import cosine_similarity
# use numpy and scikit-learn vectorized implementations for performance
simple_sim = cosine_similarity(keyword_vectors, topic_vectors)
topic_idx = simple_sim.argmax(axis=1)
print(simple_sim)

for k, i in zip(keywords, topic_idx):
  print('"%s" is about %s' % (k, topic_labels[i]))
