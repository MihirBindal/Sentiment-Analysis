from tweepy import Cursor
from twitter_credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy
import csv
import _json

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


def insert_to_csv(hashtag_phrase):
    with open("tweet_output.csv", "w", encoding="utf-8") as file:
        w = csv.writer(file)
        w.writerow(["timestamp", "tweet_text", "username", "all_hashtags", "followers_count"])
        for tweet in Cursor(api.search, q=hashtag_phrase + "-filter:retweets", lang="en", tweet_mode="extended").items(
                100):
            w.writerow([tweet.created_at, tweet.full_text.replace("\n", "").encode("utf-8"),
                        tweet.user.screen_name.encode("utf-8"),
                        [e["text"] for e in tweet._json["entities"]["hashtags"]], tweet.user.followers_count])


if __name__ == '__main__':
    insert_to_csv("#coronavirus AND #corona")
# posts = api.user_timeline(screen_name="BillGates", count=25, lang="en", tweet_mode="extended")
