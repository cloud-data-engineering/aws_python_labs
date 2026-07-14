import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Some debugging information")
logging.info("App started")
logging.warning("Disk space is low")
logging.error("File could not be opened")
logging.critical("The service is unavailable")