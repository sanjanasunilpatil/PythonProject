# importing libraries
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

# Importing dataset
dataset = pd.read_csv('../inputFiles/Restaurant_Reviews.tsv', delimiter='\t', quoting=3)

# Cleaning of Data
nltk.download('stopwords')
updated_review = []

for i in range(0, len(dataset), 1):
    review = dataset.iloc[i, 0]
    review = re.sub('[^a-zA-Z]', ' ', review).lower().split()
    ps = PorterStemmer()
    temp = []
    for word in review:
        if word not in set(stopwords.words('english')):
            temp.append(ps.stem(word))
    review = ' '.join(temp)
    updated_review.append(review)

# Creating bag of words model
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(updated_review).toarray()
y_index = dataset.columns.get_loc("Liked")
y = dataset.iloc[:, y_index:(y_index+1)]


