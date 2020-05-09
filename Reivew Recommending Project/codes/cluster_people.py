import pandas as pd
import sklearn.cluster as cl

file = "people/appliances.csv"
user_column = "users"

# expects data of the form:
# user_column,category1,categoryN
# username,val1,valN
# username,val1,valN

data = pd.read_csv(file, encoding='utf-8', index_col=[user_column])

# Different clustering algorithms are available
# clustering = cl.KMeans(n_clusters=5)

# Chose MeanShift over KMeans as it does not require a set number of clusters
clustering = cl.MeanShift()
clustering.fit(data)

# clustering.labels_ now contains a list of the cluster each user belongs to
# print(kmeans.labels_)

users = data.index.tolist()
print(user_column + ", cluster")
for i in range(0, len(clustering.labels_)):
    print("\"" + str(users[i]) + "\", " + str(clustering.labels_[i]))
