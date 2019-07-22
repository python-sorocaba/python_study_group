import logging
logging.basicConfig(filename='exception_logging.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def exception_function(*args, **kwargs):
    try:
        1 / 0
    except Exception:
        logging.exception("Exception on handling exception_function with args=%r kwargs=%r", args, kwargs)


exception_function()
