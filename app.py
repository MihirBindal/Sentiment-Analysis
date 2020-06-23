import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import data_cleaning
import get_tweets

st.title("Twitter Sentiment Analysis")
st.write("This application does the sentiment analysis of a twitter hashtag or keyword."
         "It does that by taking the recent 300 tweets from that topic/hashtag.")
st.markdown("<sub>Extracting 300 tweets and cleaning them takes time so please wait for a minute or two</sub>",
            unsafe_allow_html=True)
phrase = st.text_input("enter the hashtag or the keyword")

activities = ["Histogram of Positive, Negative and Neutral tweets", "Polarity-Subjectivity Scatterplot",
              "Top five Positive tweets", "Top five Negative tweets"]
choice = st.selectbox("Select Your Activity", activities)
if phrase is not "":
    get_tweets.insert_to_csv(hashtag_phrase=phrase)
    st.success("Scraping successful. Cleaning and formatting data...")
    data_cleaning.clean_data()

    plt.style.use('fivethirtyeight')
    df = pd.read_csv("output file\/cleaned_output.csv")


    def getSubjectivity(text):
        return float(TextBlob(text).sentiment.subjectivity)


    def getPolarity(text):
        return float(TextBlob(text).sentiment.polarity)


    def getAnalysis(score):
        if score < 0:
            return "Negative"
        elif score == 0:
            return "Neutral"
        else:
            return "Positive"


    df['Subjectivity'] = df["tweet_text"].apply(getSubjectivity)
    df['Polarity'] = df["tweet_text"].apply(getPolarity)
    df['PosNeg'] = df['Polarity'].apply(getAnalysis)
    df.to_csv(r"output file\/final_output.csv")


    def polarity_subjectivity():
        fig = plt.figure(figsize=(10, 9))
        for i in range(0, df.shape[0]):
            plt.scatter(df["Polarity"][i], df["Subjectivity"][i], color='Blue')
        plt.title('Polarity-Subjectivity Scatterplot')
        plt.xlabel('Polarity')
        plt.ylabel('Subjectivity')
        st.write(fig)


    def hist():
        fig = plt.figure(figsize=(10, 13))
        plt.title('Histogram of Positive, Negative and Neutral tweets')
        plt.xlabel('Sentiment')
        plt.ylabel('Counts')
        df['PosNeg'].value_counts().plot(kind='bar')
        plt.show()
        st.write(fig)


    def positive_tweets():
        st.write('Printing top five positive tweets:\n')
        j = 0
        i = 0
        sortedDF = df.sort_values(by=['Polarity'])
        while j < 5:
            if sortedDF['PosNeg'][i] == 'Positive':
               st.write(str(j + 1) + ') ' + sortedDF['tweet_text'][i])
               j = j + 1
            i += 1


    def negative_tweets():
        st.write('Printing top five negative tweets:\n')
        j = 0
        i = 0
        sortedDF = df.sort_values(by=['Polarity'], ascending=False)
        while j < 5:
            if sortedDF['PosNeg'][i] == 'Negative':
                st.write(str(j + 1) + ') ' + sortedDF['tweet_text'][i])
                j = j + 1
            i += 1


    if choice == "Histogram of Positive, Negative and Neutral tweets":
        hist()
    elif choice == "Polarity-Subjectivity Scatterplot":
        polarity_subjectivity()
    elif choice == "Top five Positive tweets":
        positive_tweets()
    elif choice == "Top five Negative tweets":
        negative_tweets()

    st.markdown("<sub>Note: This application uses NLP to classify tweets thus if the tweets contain words from "
                "languages other than English or contain a lot of short-forms, they may not be properly "
                "classified</sub>", unsafe_allow_html=True)
