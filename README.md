# Sentiment Analysis and Data Visualisation
 
 This repository has the code for sentiment analysis and data visualisation. This code uses Twitter API to get tweets from twitter, clean it, and then do sentiment analysis on the tweets along with some data visualisations. 

I have created two folders- one contains the code and another one conatains output csv files.

The code files includes three python files.I could've very well write all the code in a single file but I made three different files because it becomes easier to understand and work with. Also, this will help in understanding the proper pipeline to do data analysis. The three files in code directory are:-

1) get_tweets.py - This script uses Twitter API to get the tweets. You get an option to enter a keyword or hashtag for which, this script takes 300 most recent tweets and stores them in tweet_output.csv file. 

2) data_cleaning.py - This script cleans the twitter text to remove all the @username and #topics along with links to the tweet. It also removes the emojis as they cause problem in further analysis. It's output is stored in cleaned_output.csv file.

3) analysis.oy - This script does the main task of doing sentiment analysis using textblob library. Along with doing sentiment analysis, it also does some visualisation and gives some output so that we can get a better idea of the data we are working with. Note that textblob can only recognize English and thus will produce inaccurate outputs when tweets contain words from other language. The final output is stored in final_output.csv file.

Let's take an example to see how it works. 

![](2020-05-19-18-44-36.png)

First, I run get_tweets.py then give #motivation when asked for input.   