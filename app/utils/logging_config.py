import logging

def setup_logging(app):
    logging.basicConfig(
        filename='portfolio.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )