
"""sample class

    """

import logging
import logging.config
import os
import time
from logging_wrapper import logging_wrapper


class SampleClass:

    print(__name__)
    configfile_path = os.path.join(os.path.dirname(__file__), "logging.conf")
    logging.config.fileConfig(configfile_path)
    logger = logging.getLogger(__name__)

    @classmethod
    def add(cls, x, y):
        cls.logger.debug("add method start")
        return x+y

    @classmethod
    @logging_wrapper
    def add2(self, x, y):
        return x+y

    @classmethod
    @logging_wrapper
    def sum(self, x):
        sum = 0
        for tmp in range(x):
            sum += tmp
        return sum


if __name__ == "__main__":
    print(SampleClass.add(1, 2))
