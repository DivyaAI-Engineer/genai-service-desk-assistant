import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class TicketClassifier:

    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train(self, csv_file):

        df = pd.read_csv(csv_file)

        X = self.vectorizer.fit_transform(
            df["description"]
        )

        y = df["category"]

        self.model.fit(X, y)

    def predict(self, text):

        X = self.vectorizer.transform([text])

        return self.model.predict(X)[0]
