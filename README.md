# Random Forest Twitter Bot

Deployment code for [this bot](https://twitter.com/randoforestbot). Interfaces with the Twitter API through the fabulous [tweepy](https://www.tweepy.org/) library.

A hacky weekend project so tread lightly! Look below for [some tips](#making-your-own-bot) if you're looking to make your own. Additionally, feel free to shoot me a message.

#### Deploying This Project

- You'll need to `cp config/secrets_template config/secrets` and use you Twitter developer api & access key credentials.
- Run by `make start`

## Making Your Own Bot

It should be pretty easy to adjust this project for your needs if your bot is simple i.e. if it:
- can use a standard schedule
- doesn't need to respond to @
- doesn't need user input to generate tweets

#### Customize Tweet Content

Take a look at the class `BotTweet` in `src/tweet/compose.py` - the idea there is to abstract away the details of the tweepy API.

For example, if all you wanted to do is change what text the bot generates, you could just change the code in the `generate()` class method.

#### Customize Run Behavior

The script that runs as a daemon in the container is `src/app.py`, so check that out too. None of it should be dependent on the *content* of the tweets, but I haven't extensively tested it.
