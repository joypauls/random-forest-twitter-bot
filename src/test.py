from config import (
    api,
    logger,
    scheduler
)
from tweet import Bot
from tweet.generate import generate_forest
from .app import beep_boop


if __name__ == "__main__":
    logger.info("Beep boop bot booted.")
    beep_boop(is_test=True)
