from log import Log
import os

general_logger = Log()
files = [i[:-3] for i in os.listdir('.') if "manager" not in i]
sub_logger = dict()

for file in files:
    sub_logger[file] = general_logger._create_logger(file, file + ".log")
