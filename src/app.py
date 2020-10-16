import logging
import tweepy
from config import TWITTER_API_KEY, TWITTER_API_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def main():
    logger.info("script started")
    response = api.update_status("this is a forest 🌲🌲🌲")
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

    logger.info("script ended")

if __name__ == "__main__":
    main()
