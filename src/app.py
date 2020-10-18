import logging
import tweepy
from config import TWITTER_API_KEY, TWITTER_API_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
from tweet.generate import generate_forest

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def main():
    
    logger.info("script started")

    # send tweet
    new_tweet_text = generate_forest()
    _response = api.update_status(new_tweet_text)
    
    # print latest tweet for validation
    public_tweets = api.home_timeline()
    # is this a list or just iterable?
    print(public_tweets[0].text)

    logger.info("script ended")

if __name__ == "__main__":
    main()
