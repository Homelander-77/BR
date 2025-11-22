from log import Log


def loggers(func):
    def wrapper(self, *args, **kwargs):
        if not self.main_logger and not self.sub_loggers:
            await self.create_loggers(self)
    return wrapper


class LoggerManager(Log):
    @loggers
    def __init__(self):
        super().__init__()
        self.main_files = ["server", "session", "database"]
        self.sub_files = ["login", "recommendations", "registration"]
        self.main_loggers = []
        self.sub_loggers = []

    async def create_loggers(self):
        for file in self.main_files:
            self.main_logger.append(
                self._create_logger(name=file, file=file + ".log"))

        for file in self.sub_loggers:
            self.sub_loggers.append(
                self._create_logger(name=file, file=file + ".log"))
