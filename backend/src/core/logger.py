# Built-in Dependencies
from logging.handlers import RotatingFileHandler
import logging
import os

# Local Dependencies
from src.core.config import settings

# Constants
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Default log file name
LOG_FILE_NAME = "api"

# Constructing log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, f"{LOG_FILE_NAME}.log")

# Logging level and format constants
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Configuring the basic logging settings
logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

# Configuring a rotating file handler for logging
file_handler = RotatingFileHandler(filename=LOG_FILE_PATH, maxBytes=10485760, backupCount=5)
file_handler.setLevel(level=LOGGING_LEVEL)
file_handler.setFormatter(fmt=logging.Formatter(fmt=LOGGING_FORMAT))

# Configuring a console handler for logging
console_handler = logging.StreamHandler()
console_handler.setLevel(level=logging.INFO)
console_handler.setFormatter(fmt=logging.Formatter(fmt=LOGGING_FORMAT))

# Adding both handlers to the root logger
root_logger = logging.getLogger(name="")
root_logger.handlers.clear()
root_logger.addHandler(hdlr=file_handler)
root_logger.addHandler(hdlr=console_handler)


# Function to configure logging with a custom log file name
def configure_logging(log_file: str = LOG_FILE_NAME) -> None:
    """
    Configure logging with a custom log file name.

    Args:
        log_file (str): The custom log file name (without extension). Defaults to 'app'.
    """
    # Clear all handlers from the root logger
    root_logger.handlers.clear()

    # Constructing log file path based on the provided log_file parameter
    log_file_path = os.path.join(LOG_DIR, f"{log_file}.log")

    # Configuring a rotating file handler for logging
    custom_file_handler = RotatingFileHandler(
        filename=log_file_path, maxBytes=10485760, backupCount=5
    )
    custom_file_handler.setLevel(level=LOGGING_LEVEL)
    custom_file_handler.setFormatter(fmt=logging.Formatter(fmt=LOGGING_FORMAT))

    # Configuring a console handler for logging
    custom_console_handler = logging.StreamHandler()
    custom_console_handler.setLevel(level=logging.INFO)
    custom_console_handler.setFormatter(fmt=logging.Formatter(fmt=LOGGING_FORMAT))

    # Adding both handlers to the root logger
    root_logger.addHandler(hdlr=custom_file_handler)
    root_logger.addHandler(hdlr=custom_console_handler)


# Example usage of configure_logging with a custom log file name
# configure_logging(log_file='worker')
# logger = logging.getLogger(__name__)

# Don't use the 'configure_logging' function when generating 'api' logs, as 'api.log' is already the default log file.
