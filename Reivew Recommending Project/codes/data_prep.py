import pandas as pd
import gzip
import json
import os

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')
def clean(df):
    return df[['overall','verified','reviewTime','asin','reviewerName','reviewText','summary','vote']]

#df_appliances = getDF('Appliances_5.json.gz')
#df_appliances = clean(df_appliances)
#df_appliances.to_csv(r'/Users/yunluli/Desktop/IR Project/data/Appliances.csv', index=False, header=True)

directory = r'/Users/yunluli/Desktop/IR Project/json/'
for jFile in os.listdir(directory):
    if jFile.endswith("json.gz"):
        df=getDF(os.path.join(directory, jFile))
        df=clean(df)
        name, extension = jFile.split('_5')
        df.to_csv(r'/Users/yunluli/Desktop/IR Project/data/'+name+'.csv', index=False, header=True)
        print(jFile)
