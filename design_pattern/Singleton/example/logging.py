'''
implementations of logger file
'''
import logging


class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.logger = logging.getLogger(__name__)
            cls.__instance.logger.setLevel(logging.DEBUG)
            handler = logging.FileHandler('log.txt')
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(leveltime)s - %(message)s')
            handler.setFormatter(formatter)
            cls.__instance.logger.addHandler(handler)
        return cls.__instance


logger = Logger().logger

logger.info("This is a log message")


class Config:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.settings = {
                'debug': True,
                'max_threads': 8,
                'timeout': 60
            }
        return cls.__instance


config = Config().settings

debug_mode = config['debug']
max_threads = config['max_threads']
timeout = config['timeout']
