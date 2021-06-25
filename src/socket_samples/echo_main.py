import logging, logging.handlers
from logging.handlers import QueueHandler, QueueListener
import queue
from tqdm import tqdm
import time

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)
socket_handler = logging.handlers.SocketHandler('192.168.1.12',
                    5000)
que = queue.Queue(-1)
queue_handler = QueueHandler(que)
listener = QueueListener(que, socket_handler)
# don't bother with a formatter, since a socket handler sends the event as
# an unformatted pickle
rootLogger.addHandler(queue_handler)

# handler = logging.StreamHandler()
# handler.setFormatter(logging.Formatter('%(asctime)s : ' +logging.BASIC_FORMAT))
# rootLogger.addHandler(handler)

listener.start()

for i in tqdm(range(5)):
    # Now, we can log to the root logger, or any other logger. First the root...
    logging.info('Jackdaws love my big sphinx of quartz.')

    # Now, define a couple of other loggers which might represent areas in your
    # application:

    logger1 = logging.getLogger('myapp.area1')
    logger2 = logging.getLogger('myapp.area2')
    logger1.debug('Quick zephyrs blow, vexing daft Jim.')
    logger1.info('How quickly daft jumping zebras vex.')
    logger2.warning('Jail zesty vixen who grabbed pay from quack.')
    logger2.error('The five boxing wizards jump quickly.')

print("finish!!")
listener.stop()