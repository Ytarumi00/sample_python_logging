import logging


def some_method1():

    print("#--start some_method1--#")

    logger = logging.getLogger(__name__)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

    print("#--end some_method1--#")


if __name__ == '__main__':
    some_method1()
