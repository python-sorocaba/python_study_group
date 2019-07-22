import logging
logging.basicConfig(filename='simple_logging.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def my_beautiful_function():
    logging.debug("Enter on function!")
    print("Hello!")


my_beautiful_function()
