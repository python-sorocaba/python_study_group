import logging
logging.basicConfig(filename='using_exc_info.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def exception_function(*args, **kwargs):
    try:
        1 / 0
    except Exception:
        logging.fatal(
            "Exception on handling exception_function with args=%r kwargs=%r",
            args,
            kwargs,
            exc_info=True,
        )


exception_function()
