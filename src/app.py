from config import (
    api,
    logger,
    scheduler
)
from tweet import BotTweet

# hours
TWEET_INTERVAL = 7
# num lines
GRID_HEIGHT = 7
# width in tokens
GRID_WIDTH = 12


def new_bot_tweet():
    bot = BotTweet(api, GRID_HEIGHT, GRID_WIDTH)
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
    new_bot_tweet()

    # add job
    _job = scheduler.add_job(new_bot_tweet, "interval", hours=TWEET_INTERVAL)
    # start scheduler as primary foreground process
    scheduler.start()


if __name__ == "__main__":
    logger.info("bot started")
    main()
