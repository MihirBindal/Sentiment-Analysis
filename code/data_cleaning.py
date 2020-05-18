import pandas as pd
import numpy as np
import re
import textblob as Textblob
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

df = pd.read_csv("..\output file\/tweet_output.csv")
print(df["tweet_text"][186])
i = 0
for n in df["tweet_text"]:
    df["tweet_text"][i] = re.sub(r'\\..[\w0-9]', '', df["tweet_text"][i])
    df["tweet_text"][i] = re.sub(r'#\w*', '', df["tweet_text"][i])
    df["tweet_text"][i] = re.sub(r'https?://[\w.]*/?.........[\w\d]', '', df["tweet_text"][i])
    df["tweet_text"][i] = re.sub(r'@\w*', '', df["tweet_text"][i])
    df["tweet_text"][i] = re.match(r"^b('|\")([\w\d\s?\.,&;!-_\+\*\\\|\@\#\$\%\^\&\*~`]*)('|\")$",
                                   df["tweet_text"][i]).group(2)
    df["username"][i] = re.match(r"^b('|\")([\w\d\s?\.,&;!-_\+\*\\\|\@\#\$\%\^\&\*~`]*)('|\")$",
                                 df["username"][i]).group(2)
    df["length_of_tweet"][i] = len(df["tweet_text"][i])
    i += 1
df.to_csv(r"..\output file\/cleaned_output.csv")
print("The code is running....")
print("Pay no heed to those red lines, they are warnings.")