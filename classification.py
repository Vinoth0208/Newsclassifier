import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import streamlit as st

def classify():
    df=pd.read_csv(r'NewsData.csv')
    df.dropna(inplace=True)
    X = df['title']
    y = df['category']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 80)

    lr = Pipeline([('vect', CountVectorizer()),
                   ('tfidf', TfidfTransformer()),
                   ('clf', LogisticRegression(max_iter = 1000)),
                  ])

    lr.fit(X_train,y_train)
    y_pred = lr.predict(X_test)

    print(f"Accuracy is : {accuracy_score(y_pred,y_test)}")

    news = []
    inputtext=st.text_area('Input news to classify')
    for x in inputtext.split('\n'):
        news.append(x)
    submit=st.button('Submit')
    if submit:
        predicted = lr.predict(news)

        for doc, category in zip(news, predicted):
            st.write(category)