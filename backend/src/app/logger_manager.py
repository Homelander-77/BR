from log import Log


def loggers(func):
    def wrapper(self, *args, **kwargs):
        if not self.main_logger and not self.sub_logger:
            func(self, *args, *kwargs)
    return wrapper


class LoggerManager(Log):
    def __init__(self):
        super().__init__()
        self.general_name = "general"
        self.main_files = ["server", "session", "database"]
        self.sub_files = ["login", "recommendations", "registration"]
        self.general_logger = self._create_logger(
            name=self.general_name, file=self.general_name + ".log"
            )
        self.main_logger = {}
        self.sub_logger = {}
        self.create_loggers()

    @loggers
    def create_loggers(self):
        for file in self.main_files:
            self.main_logger[file] = self._create_logger(
                name=file, file=file + ".log")

        for file in self.sub_logger:
            self.sub_loggers[file] = self._create_logger(
                name=file, file=file + ".log")


l = LoggerManager()
