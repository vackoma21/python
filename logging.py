import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(
    format=FORMAT,
    level=logging.INFO
)
logging.warning("Ahoj")