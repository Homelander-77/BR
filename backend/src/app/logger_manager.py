from log import Log
import os

l = Log()
general_logger = l.general_logger


main_logger = dict()
for main_file in ["server", "session", "database"]:
    main_logger[main_file] = l._create_logger(
        main_file, main_file + ".log"
        )



sub_files = [
    i[:-3] for i in os.listdir('.')
    if "manager" not in i
    ]
sub_logger = dict()
for sub_file in sub_files:
    sub_logger[sub_file] = l._create_logger(
        sub_file, sub_file + ".log"
        )
