import json

import tweepy
import logging
import os
import snscrape.modules.twitter as sntwitter


def snscrape_twitter_tweets(twitter_user_name: str, num_tweets: int = 5):
    scrapper = sntwitter.TwitterUserScraper(twitter_user_name)
    output_filename = twitter_user_name + ".txt"
    with open(output_filename, "w") as f:
        for i, tweet in enumerate(scrapper.get_items(), start=1):
            tweet_json = json.loads(tweet.json())
            print(f"\n Scrapped Tweet: {tweet_json['content']}")
            f.write(tweet.json())
            f.write("\n")
            f.flush()
            if num_tweets and i > num_tweets:
                break


def scrape_twitter_tweets(twitter_user_name: str, num_tweets: int = 5):
    consumer_key = "fHqIiab3J4rAJKzVubhpGK8AU"
    consumer_secret = "ODxRPijjNOE3m1vqzgvic6nkZ7qLybvLANe3AedAJSbSSzM2Gg"
    access_token = "1704834563942547456-j8Dah9rK0ZYRZtYlNtewDSAdcDQJXG"
    access_token_secret = "M3VnaGaQTqk9qeIxLhGJIiJY8dTEVlkLHw4pkVEl6S5eV"
    client_id = os.getenv("TWITTER_CLIENT_ID")
    client_secret = os.getenv("TWITTER_CLIENT_SECRET")

    access_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOBLqAEAAAAArJVI%2Fg%2BTDwOMgDqlS9jln24ZLnc%3DDHFB8BhHRMG92NCzms0dH2ymOjgSV1EKCVsxpepOBaiEf01ruM"

    client = tweepy.Client(
        bearer_token=access_BEARER_TOKEN,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    # logger = logging.getLogger("twitter")
    # auth = tweepy.OAuthHandler(
    #     consumer_key, consumer_secret
    # )
    # auth.set_access_token(
    #     access_token, access_token_secret
    # )
    #
    #
    # api = tweepy.API(auth)
    #
    # tweets = api.user_timeline(screen_name= "@elonmusk", count=num_tweets)
    # tweet_list=[]
    # for tweet in tweets:
    #     if "RT @" not in tweet.text and not tweet.text.startswith("@"):
    #         tweet_list.append(tweet.text)
    #
    # print(tweet_list)

    user_id = client.get_user(username=twitter_user_name).data.id

    tweets = client.get_users_tweets(
        id=user_id, exclude=["retweets", "replies"], max_results=100
    )
    print(tweets)
    tweet_list = []
    for tweet in tweets.data:
        tweet_dict = {}
        tweet_dict["text"] = tweet["test"]
        tweet_dict["URL"] = f"https://twitter.com/{twitter_user_name}/status/{tweet.id}"
        tweet_list.append(tweet_dict)

    print(tweet_list)

    return tweet_list
