import logging
import queue
import time
from logging.handlers import QueueHandler, QueueListener

if __name__ == '__main__':
    print('main')
    que = queue.Queue(-1)
    queue_handler = QueueHandler(que)
    handler = logging.StreamHandler()
    listener = QueueListener(que, handler)

    logger = logging.getLogger(__name__)
    logger.propagate=False
    logger.addHandler(queue_handler)
    formatter = logging.Formatter('%(thread)s: %(message)s')
    handler.setFormatter(formatter)
    
    root = logging.getLogger()
    root.addHandler(handler)

    listener.start()

    logger.warning('Look out!')
    time.sleep(10)
    logging.warning('root')

    listener.stop()