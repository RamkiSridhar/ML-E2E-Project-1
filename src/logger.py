import logging 
import os 
from datetime import datetime 

#Log file naming:
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory (ONLY directory here)
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok= True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH, 
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level= logging.INFO, 
    force= True
)

#TESTING:

# if __name__ == '__main__':
#     logging.info("Logging has started.")