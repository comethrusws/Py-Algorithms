from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# abo Split dataset lai into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(newsgroups.data, newsgroups.target, test_size=0.2, random_state=42)

# TF-IDF vectorizer and an svm classifier create garne
vectorizer = TfidfVectorizer()
svm_classifier = SVC(kernel='linear')

model = make_pipeline(vectorizer, svm_classifier)

# train the model
model.fit(X_train, y_train)

# make predictions on the test set
y_pred = model.predict(X_test)

#evaluation
report = classification_report(y_test, y_pred, target_names=newsgroups.target_names)
print(report)
