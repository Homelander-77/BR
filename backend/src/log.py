import logging
import os


format_log = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


def logger_existing(func):
    def wrapper(self, *args, **kwargs):
        if kwargs["name"] in logging.Logger.manager.loggerDict:
            return logging.getLogger(kwargs["name"])
        return func(self, *args, **kwargs)


class Log:
    def __init__(self):
        self.logs_folder = '/server/logs'
        os.makedirs(self.logs_folder, exist_ok=True)
        self.general_file = os.path.join(self.logs_folder, "general.log")
        self.general_logger = self._create_logger("general", self.general_file)

    @logger_existing
    def _create_logger(self, name: str, file: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        file_handler = logging.handlers.RotatingFileHandler(
            file, maxBytes=5_000_000, backupCount=2)
        file_handler.setFormatter(logging.Formatter(
            format_log
        ))

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            format_log
         ))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger

    def get_module_logger(self, module_name: str) -> logging.Logger:
        filename = os.path.join(self.logs_folder, f"{module_name}.log")
        logger = self._create_logger(name=module_name, file=filename)
        return logger
