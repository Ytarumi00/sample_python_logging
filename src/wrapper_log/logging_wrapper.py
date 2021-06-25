
def logging_wrapper(func):
    import functools
    import logging
    import datetime
    logger = logging.getLogger(__name__)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()

        logger.info("start: {}".format(func))
        logger.debug("param: {}, {}".format(args, kwargs))
        res = func(*args, **kwargs)
        logger.debug("return: {}".format(res))
        logger.info("end: {}".format(func))

        end_time = datetime.datetime.now()
        logger.debug("process time: {}".format(end_time - start_time))
        return res

    return wrapper
