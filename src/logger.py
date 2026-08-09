import logging 
import os
from datetime import datetime 

# create log file:
    # datetime.now() select the log file time for now and store in the format 
        # day, month, year, hour, min, sec (file suffix.log)
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# save the file int he log_path - current working directory (CWD) called: logs; then the name of the logfile
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# save in a directory, if that doesn't exist, then make the directory in the log path (designated) 
# save the log file in it 
# exist_ok - even if there are files in the current log file, keep appending them to this current file, dont replace previous logs
os.makedirs(log_path, exist_ok= True) 

#full path where it will be saved
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

#ignore debugs - basicconfig =  but put everything else above info into a log file 
logging.basicConfig(
    filename = LOG_FILE_PATH,
    #format of file: time stamp, line number, name, level name (error/sucess name), message itself
    format = "[ %(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s",

#level = logging.INFO sets the minimum severity threshold
    # AKA what gets written to your log file.
    # python logging systems has 5 standard levels of severity - lowest to highest:
        #debug, info, warning, error, critical (10,20,30,40,50)

    level = logging.INFO
)


#following checks if it works - you called logging.info() the statement is logging has started
    # log file will form and the line number, file, etc will be stated

if __name__ == '__main__':
    logging.info("logging has started")
