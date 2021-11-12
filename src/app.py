from config import (
    api,
    logger,
    scheduler
)
from tweet import Bot
from tweet.generate import generate_forest

# class Bot():
#     """
#     The bot
#     """
#     def __init__(
#         self,
#         api: tweepy.API,
#         generator: Callable[[int, int], str], 
#         height: int,
#         width: int,
#         is_test: bool = False
#     ):
#         self.api = api
#         self.height = height
#         self.width = width
#         self.is_test = is_test
#         self.text = None

#     def generate(self):
#         self.text = self.generator(self.height, self.width)

# hours
TWEET_INTERVAL = 6
# num lines
GRID_HEIGHT = 7
# width in tokens
GRID_WIDTH = 12


def beep_boop(is_test: bool = False):
    bot = Bot(api, generate_forest, GRID_HEIGHT, GRID_WIDTH, is_test)
    try:
        # generate the actual text
        bot.generate()
        # send with tweepy api
        bot.send()
        # log latest tweet to validate
        # last = bot.get_last()
        # print(last)
    except Exception as e:
        print(e)
        logger.error("failed to send tweet")


def main():
    # uncomment for adhoc run at start
    beep_boop()
    # add job
    _job = scheduler.add_job(beep_boop, "interval", hours=TWEET_INTERVAL)
    # start scheduler as primary foreground process
    scheduler.start()


if __name__ == "__main__":
    logger.info("Beep boop bot booted.")
    main()
