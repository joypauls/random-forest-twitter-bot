import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

def main():
    logger.info("scheduler started")

if __name__ == "__main__":
    main()
