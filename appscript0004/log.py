import logging

class Log:
    def __init__(self):
        self.logger = logging.getLogger('appscript0004')
        self.logger.setLevel(logging.INFO)

    def log(self, message):
        self.logger.info(message)