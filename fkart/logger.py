import logging


class Logger:
    @classmethod
    def _setup_logger(cls, log_filename=None):
        if not logging.getLogger().hasHandlers():  # Prevents reinitializing the logger
            if log_filename:
                logging.basicConfig(level=logging.DEBUG, filename=log_filename, filemode="w",
                                    format="%(asctime)s - %(message)s")
            else:
                logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")
        return logging.getLogger()

    @classmethod
    def requests_error(cls, exception, log_filename=None):
        logger = cls._setup_logger(log_filename)
        logger.exception(f"Error: {exception} occurred while loading product URL")

    @classmethod
    def bs4_error(cls, exception, log_filename=None):
        logger = cls._setup_logger(log_filename)
        logger.exception(f"Error: {exception} occurred while extracting product price from HTML content.\n"
                         "You might want to have a look at price_identifier in consts.py")
