import logging

print("print")

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.info("So should thid")
logging.warning("And this, too")
logging.error("And non-ASCII stuff, too, like Oresund and Malmo")