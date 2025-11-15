from log import Log
import os

logger = Log()
files = [i for i in os.listdir('.') if "manager" not in i]
sub_logger = dict()

for file in files:
    sub_logger[file] = logger._create_logger(file, file + ".log")

