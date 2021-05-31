import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def do_something():

    logger.propagate = True
    logger.info("do something #{}: {}".format(1, "propagate=True"))
    logger.debug("do something #{}: {}".format(2, "propagate=True"))

    # propagate=Flaseのためmainから呼び出した場合は表示されない
    logger.propagate = False
    logger.info("do something #{}: {}".format(3, "propagate=True"))
    logger.debug("do something #{}: {}".format(4, "propagate=False"))

    pass


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
    logger.addHandler(handler)
    do_something()
