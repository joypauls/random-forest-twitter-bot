"""
Main interface to generate a tweet for the bot.
"""
import tweepy
from typing import Callable
from config import logger
from tweet.generate import generate_forest


class Bot():
    """
    Tweet generator class
    """
    def __init__(
        self,
        api: tweepy.API,
        generator: Callable[[int, int], str], 
        height: int,
        width: int,
        is_test: bool = False
    ):
        self.api = api
        self.generator = generator
        self.height = height
        self.width = width
        self.is_test = is_test
        self.text = None

    def generate(self):
        self.text = self.generator(self.height, self.width)

    def send(self):
        if self.text is None:
            logger.error("self.text cannot be None")
        else:
            if self.is_test:
                logger.info("sending tweet (test)...")
                logger.info(self.text)
                logger.info("tweet sent (test)")
            else:
                logger.info("sending tweet...")
                _response = self.api.update_status(self.text)
                logger.info("tweet sent")

    def get_last(self) -> str:
        logger.info("displaying latest tweet")
        latest_public_tweets = self.api.home_timeline()
        return latest_public_tweets[0].text
