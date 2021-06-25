import os
import logging
import logging.config

configfile_path = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(configfile_path)

# create logger
logger = logging.getLogger('simpleExample')

# application code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


logging.debug("root debug")
logging.info("root info")
