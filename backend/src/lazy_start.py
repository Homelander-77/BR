def lazy_start(method):
    def wrapper(self, *args, **kwargs):
        if self.conn is None:
            self.connect()
        return method(self, *args, **kwargs)
    return wrapper
