from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


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
