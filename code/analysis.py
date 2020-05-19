from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
df = pd.read_csv("..\output file\/cleaned_output.csv")


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
df.to_csv(r"..\output file\/final_output.csv")

print('Printing positive tweets:\n')
j = 1
sortedDF = df.sort_values(by=['Polarity'])
for i in range(0, sortedDF.shape[0]):
    if sortedDF['PosNeg'][i] == 'Positive':
        print(str(j) + ') ' + sortedDF['tweet_text'][i])
        print()
        j = j + 1

print('Printing negative tweets:\n')
j = 1
sortedDF = df.sort_values(by=['Polarity'], ascending=False)
for i in range(0, sortedDF.shape[0]):
    if sortedDF['PosNeg'][i] == 'Negative':
        print(str(j) + ') ' + sortedDF['tweet_text'][i])
        print()
        j = j + 1

plt.figure(figsize=(8, 6))
for i in range(0, df.shape[0]):
    plt.scatter(df["Polarity"][i], df["Subjectivity"][i], color='Blue')
plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()

print(df['PosNeg'].value_counts())

plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['PosNeg'].value_counts().plot(kind = 'bar')
plt.show()