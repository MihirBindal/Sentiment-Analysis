from tweepy import Cursor
import tweepy
import csv
ACCESS_TOKEN= '2416039333-DBU1WNwPFMhnG2e4BVXz8KhVcHyUJzfQQVLjTcX'
ACCESS_TOKEN_SECRET= 'vvSbcXTBs2qODaI9cLDCrlRTrdyLIRsSNEoMdC63kb5mk'

CONSUMER_KEY= 'IumY4QH863vr56xQiFj6FWEuz'
CONSUMER_SECRET= 'ufwIXYsTZN8YFELbL5CYmPCsZZtnFnIBqz6DPO1pLOhZ2RpxiP'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


def insert_to_csv(hashtag_phrase):
    with open("tweet_output.csv", "w", encoding="utf-8") as file:
        w = csv.writer(file)
        w.writerow(["timestamp", "tweet_text", "username", "all_hashtags", "followers_count", "favorite_count",
                    "retweets_count", "length_of_tweet"])
        for tweet in Cursor(api.search, q=hashtag_phrase + "-filter:retweets", lang="en", tweet_mode="extended").items(
                300):
            w.writerow([tweet.created_at, tweet.full_text.replace("\n", "").encode("utf-8"),
                        tweet.user.screen_name.encode("utf-8"),
                        [e["text"] for e in tweet._json["entities"]["hashtags"]], tweet.user.followers_count,
                        tweet.favorite_count, tweet.retweet_count,
                        len(tweet.full_text.replace("\n", "").encode("utf-8"))])

