import logging
import logging.config


logging.basicConfig(level=logging.DEBUG)
logging.config.fileConfig('./fileconfig/logging2.conf')

#create logger
logger = logging.getLogger('simpleExample')

#application code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


logging.debug("root debug")
logging.info("root info")