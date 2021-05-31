import logging
from logging import getLogger

#create logger
logger = getLogger('simple_example')
logger.setLevel(logging.INFO)

#create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#create formatter
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#add formatter to ch
#ch.setFormatter(formatter)

#add ch to logger
logger.addHandler(ch)

#application code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')