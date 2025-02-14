import logging  # to log the messages which helps in debugging and tracking program execution
import os # to interact with the operating system
from datetime import datetime #to handle the date and time

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # generating the log files with timestamp
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #creating the directory path for logs
os.makedirs(logs_path,exist_ok=True) #Creating the Logs Directory if It Doesn't Exist

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



