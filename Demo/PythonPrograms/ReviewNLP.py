# importing libraries
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

# Split data into training and test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Fit data into model
classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)

# Predict data using model
y_pred = classifier.predict(x_test)

# Calculate accuracy of model
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)


