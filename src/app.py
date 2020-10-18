import logging
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
from config import TWITTER_API_KEY, TWITTER_API_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
from tweet.generate import generate_forest

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)
logger.addHandler(logging.StreamHandler())

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

scheduler = BlockingScheduler()

def send_tweet():
    pass


def main():
    
    logger.info("script started")

    # send tweet
    new_tweet_text = generate_forest()
    _response = api.update_status(new_tweet_text)
    
    # print latest tweet for validation
    public_tweets = api.home_timeline()
    # is this a list or just iterable?
    print(public_tweets[0].text)

    # add job
    _job = scheduler.add_job(send_tweet, "interval", hours=5)
    scheduler.start()

if __name__ == "__main__":
    main()
