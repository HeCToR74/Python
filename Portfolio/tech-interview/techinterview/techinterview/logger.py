from django.conf import settings
import logging
import os


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Logger(metaclass=Singleton):
    _logger = None

    def __init__(self):
        LOG_DIR = os.path.join(settings.BASE_DIR, 'log')
        self._logger = logging.getLogger("tech-interview")
        self._logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(os.path.join(LOG_DIR, 'server.log'))
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        if not settings.DEBUG:
            self._logger.debug = lambda msg: msg
        fh.setFormatter(formatter)
        self._logger.addHandler(fh)

    def get_logger(self):
        return self._logger


log_instance = Logger()
log = log_instance.get_logger()
