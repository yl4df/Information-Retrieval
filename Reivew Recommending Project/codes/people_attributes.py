import pandas as pd

file = "review_scores/appliances.csv"

data = pd.read_csv(file, encoding='utf-8')

topics = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
users = {}


def csv_header():
    output = "users"
    for topic in topics:
        output += ", " + topic
    print(output)


# Sum up the scores for all reviews that each user has made

for index, row in data.iterrows():
    name = row['reviewerName']
    if name in users:
        users[name]['numReviews'] += 1
        for topic in topics:
            users[name][topic] += row[topic]
    else:
        user = {'numReviews': 1}
        for topic in topics:
            user[topic] = row[topic]
        users[name] = user


# Averages and prints the scores by the number of revies that each user made
csv_header()

for user in users:
    output = "\"" + str(user) + "\""
    for topic in topics:
        users[user][topic] /= users[user]['numReviews']
        output += ", " + str(users[user][topic])
    print(output)

# clustering.labels_ now contains a list of the cluster each user belongs to
# print(kmeans.labels_)


# users = data.index.tolist()
# for i in range(0, len(clustering.labels_)):
#     print(users[i] + ": " + str(clustering.labels_[i]))






    # expects data of the form:
    # user_column,category1,categoryN
    # username,val1,valN
    # username,val1,valN
