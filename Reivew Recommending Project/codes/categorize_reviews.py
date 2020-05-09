import pandas as pd
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import nltk
nltk.download('wordnet')
stemmer = SnowballStemmer("english")

dicts = [{
    "gardus": 0.023,
    "sorri": 0.018,
    "wait": 0.017,
    "husband": 0.016,
    "serious": 0.016,
    "musti": 0.016,
    "tell": 0.016,
    "bunch": 0.016,
    "sit": 0.016,
    "tear": 0.016
},
{
    "conveni": 0.054,
    "project": 0.054,
    "catcher": 0.054,
    "littl": 0.039,
    "lose": 0.039,
    "felt": 0.028,
    "wouldn": 0.028,
    "nest": 0.027,
    "contrapt": 0.027,
    "space": 0.027
},
{
    "open": 0.020,
    "mask": 0.016,
    "leaf": 0.016,
    "resist": 0.015,
    "ensur": 0.015,
    "littl": 0.015,
    "filter": 0.014,
    "unfortun": 0.012,
    "definit": 0.012,
    "unit": 0.011
},
{
    "instruct": 0.020,
    "climb": 0.020,
    "attic": 0.020,
    "buck": 0.020,
    "save": 0.015,
    "duct": 0.015,
    "push": 0.014,
    "unscrew": 0.013,
    "feet": 0.013,
    "marvel": 0.013
},
{
    "thank": 0.085,
    "element": 0.043,
    "great": 0.019,
    "project": 0.006,
    "conveni": 0.006,
    "catcher": 0.006,
    "speed": 0.005,
    "lose": 0.005,
    "clutch": 0.005,
    "gardus": 0.005
},
{
    "great": 0.093,
    "good": 0.053,
    "washer": 0.045,
    "tube": 0.040,
    "lazi": 0.034,
    "clod": 0.023,
    "foot": 0.019,
    "angl": 0.016,
    "figur": 0.016,
    "plier": 0.016
},
{
    "price": 0.209,
    "better": 0.023,
    "great": 0.019,
    "littl": 0.006,
    "project": 0.005,
    "conveni": 0.005,
    "catcher": 0.005,
    "month": 0.004,
    "quick": 0.004,
    "problem": 0.004
},
{
    "cycl": 0.073,
    "long": 0.058,
    "auto": 0.049,
    "good": 0.038,
    "run": 0.027,
    "potenti": 0.025,
    "gallon": 0.025,
    "bucket": 0.024,
    "jean": 0.024,
    "adapt": 0.024
},
{
    "speed": 0.026,
    "clutch": 0.024,
    "perfect": 0.023,
    "high": 0.022,
    "fast": 0.015,
    "water": 0.014,
    "replac": 0.013,
    "pipe": 0.013,
    "half": 0.013,
    "slow": 0.011
},
{
    "line": 0.076,
    "glad": 0.030,
    "wad": 0.030,
    "get": 0.023,
    "help": 0.022,
    "buy": 0.019,
    "free": 0.018,
    "shop": 0.017,
    "tri": 0.016,
    "necessari": 0.016
}]

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


file = "data/Appliances.csv"
data = pd.read_csv(file, encoding='utf-8')

print("reviewerName,0,1,2,3,4,5,6,7,8,9")

for index, row in data.iterrows():
    words = preprocess(str(row["reviewText"]))

    review = [0] * 10
    for word in words:
        for i in range(len(dicts)):
            if word in dicts[i]:
                review[i] += dicts[i][word]

    string = "\"" + str(row["reviewerName"]) + "\""
    for r in review:
        string += "," + str(r)

    print(string)
