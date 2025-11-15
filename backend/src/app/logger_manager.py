from log import Log
import os

general_logger = Log()


main_logger = dict()
for main_file in ["server", "session", "database"]:
    main_logger[main_file] = general_logger._create_logger(
        main_file, main_file + ".log"
        )



sub_files = [
    i[:-3] for i in os.listdir('.')
    if "manager" not in i
    ]
sub_logger = dict()
for sub_file in sub_files:
    sub_logger[sub_file] = general_logger._create_logger(
        sub_file, sub_file + ".log"
        )
