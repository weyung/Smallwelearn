import logging

logger = logging.getLogger('welearn')


logger.addHandler(logging.FileHandler('welearn.log'))
logger.handlers[0].stream = open('welearn.log', 'w', encoding='utf-8')
logger.handlers[0].setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

class LogFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)

    def format(self, record):
        if record.levelno == logging.DEBUG:
            record.msg = '[\033[94m*\033[0m] {}'.format(record.msg)
        elif record.levelno == logging.INFO:
            record.msg = '[\033[92m+\033[0m] {}'.format(record.msg)
        elif record.levelno == logging.WARNING:
            record.msg = '[\033[93m!\033[0m] {}'.format(record.msg)
        elif record.levelno == logging.ERROR:
            record.msg = '[\033[91mx\033[0m] {}'.format(record.msg)
        return super().format(record)

handler = logging.StreamHandler()
handler.setFormatter(LogFormatter())
logger.addHandler(handler)


logger.setLevel(logging.DEBUG)
