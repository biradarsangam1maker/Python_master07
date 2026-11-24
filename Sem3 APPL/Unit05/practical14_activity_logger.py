# Demonstrate the various uses of Python's logging module
import logging

logging.basicConfig(
    filename="program.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is a debug message.")
logging.info("Program started.")
logging.warning("This is a warning message.")
logging.error("An error occurred.")
logging.critical("A critical error occurred.")

print("Logging demonstration completed. Check program.log.")
