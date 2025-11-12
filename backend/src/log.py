import logging
import os


def logger_existing(func):
    def wrapper(self, *args, **kwargs):
        if kwargs["name"] in logging.Logger.manager.loggerDict:
            return None
        return func(*args, **kwargs)


class Log:
    def __init__(self):
        self.logs_folder = '/server/logs'
        self.general_file = os.path.join(self.logs_folder, "general.log")
        self.general_logger = self._create_logger("general", self.general_file)

    @logger_existing
    def _create_logger(self, name: str, file: str) -> logging.Loger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        file_handler = logging.handlers.RotatingFileHandler(
            file, maxBytes=5_000_000, backupCount=2)
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                                  ))

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                                     ))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
