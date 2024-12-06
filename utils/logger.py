from loguru import logger

logger.remove()
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} -{level}- {message}",
    )

logging = logger


if __name__=='__main__':
    
    logging.info('Logging initialised!')