import re
import sys
import nltk
import streamlit as st
from nltk import WordNetLemmatizer, PorterStemmer

nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd
sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\NewsClassifier\venv\Lib\site-packages')
from newsapi import  NewsApiClient

def datascrap():
    newsapi = NewsApiClient(api_key='deef0356cc82433aa48ff005525da9bb')

    agriculture_articles = newsapi.get_everything(q='agriculture', language='en', page_size=100)
    enterprise_journalism_articles = newsapi.get_everything(q='enterprise journalism', language='en', page_size=100)
    investigative_and_watchdog_journalism_articles = newsapi.get_everything(q='investigative and watchdog journalism', language='en', page_size=100)
    tech_articles = newsapi.get_everything(q='tech', language='en', page_size=100)
    entertainment_articles = newsapi.get_everything(q='entertainment',language='en', page_size=100)
    business_articles = newsapi.get_everything(q='business',language='en', page_size=100)
    sports_articles = newsapi.get_everything(q='sports',language='en', page_size=100)
    politics_articles = newsapi.get_everything(q='politics',language='en', page_size=100)
    travel_articles = newsapi.get_everything(q='travel',language='en', page_size=100)
    food_articles = newsapi.get_everything(q='food',language='en', page_size=100)
    health_articles = newsapi.get_everything(q='health',language='en', page_size=100)
    feature_stories_articles = newsapi.get_everything(q='feature stories',language='en', page_size=100)
    journalistic_beats_articles = newsapi.get_everything(q='journalistic beats',language='en', page_size=100)

    agriculture=pd.DataFrame(agriculture_articles['articles'])
    agriculture['category'] = 'Agriculture'
    enterprise_journalism=pd.DataFrame(enterprise_journalism_articles['articles'])
    enterprise_journalism['category'] = 'Enterprise Journalism'
    investigative_and_watchdog_journalism=pd.DataFrame(investigative_and_watchdog_journalism_articles['articles'])
    investigative_and_watchdog_journalism['category'] = 'Investigative and Watchdog Journalism'
    tech=pd.DataFrame(tech_articles['articles'])
    tech['category'] = 'Tech'
    entertainment = pd.DataFrame(entertainment_articles['articles'])
    entertainment['category'] = 'Entertainment'
    business = pd.DataFrame(business_articles['articles'])
    business['category'] = 'Business'
    sports = pd.DataFrame(sports_articles['articles'])
    sports['category'] = 'Sports'
    politics = pd.DataFrame(politics_articles['articles'])
    politics['category'] = 'Politics'
    travel = pd.DataFrame(travel_articles['articles'])
    travel['category'] = 'Travel'
    food = pd.DataFrame(food_articles['articles'])
    food['category'] = 'Food'
    health = pd.DataFrame(health_articles['articles'])
    health['category'] = 'Health'
    feature_stories = pd.DataFrame(feature_stories_articles['articles'])
    feature_stories['category'] = 'Feature Stories'
    journalistic_beats = pd.DataFrame(journalistic_beats_articles['articles'])
    journalistic_beats['category'] = 'Journalistic Beats'

    categories = [agriculture,investigative_and_watchdog_journalism, enterprise_journalism, tech, entertainment, business, sports, politics,travel, food, health, feature_stories, journalistic_beats]
    df = pd.concat(categories)

    def stem(text):
        porter_stemmer = PorterStemmer()
        nltk_tokens = nltk.word_tokenize(text)
        stemmedtext=[]
        for w in nltk_tokens:
            stemmedtext.append(porter_stemmer.stem(w))

        text = " ".join(stemmedtext)
        return text

    def lemma(text):
        lemmatizer = WordNetLemmatizer()
        nltk_tokens = nltk.word_tokenize(text)
        lemmatext = []
        for w in nltk_tokens:
            lemmatext.append(lemmatizer.lemmatize(w))

        text = " ".join(lemmatext)
        return text

    def textclean(text):

        text = re.sub(r',', '', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\.', '', text)
        text = re.sub(r"['\"]", '', text)
        text = re.sub(r'\W', ' ', text)

        text_token = word_tokenize(text)
        stop_words = set(stopwords.words('english'))

        filtered_text = []
        for sw in text_token:
            if sw not in stop_words:
                filtered_text.append(sw)

        text = " ".join(filtered_text)
        return text


    df['content'] = df['content'].apply(stem)
    df['content'] = df['content'].apply(lemma)
    df['news_title'] = df['title'].apply(textclean)

    df.to_csv(r'NewsData.csv')

    st.write(df)

    File=df.to_csv()
    st.download_button(
                label="Download data as CSV",
                data=File,
                file_name='NewsData.csv',
                mime='text/csv',)


