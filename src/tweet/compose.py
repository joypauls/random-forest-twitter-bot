from datetime import datetime

class RFBotTweet():
    """
    Create a new tweet.
    """
    def __init__(self):
        self.created_timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")