import logging
from logging.handlers import TimedRotatingFileHandler

# logging.basicConfig(
#     level=logging.INFO,  # change to DEBUG for more detail
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     datefmt="%H:%M:%S"
# )

# logger = logging.getLogger(__name__)

# ========== LOGGING CONFIG ==========
logger = logging.getLogger("ai_agent")
logger.setLevel(logging.DEBUG)  # highest level, filter in handler

# general format
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ---- Log console ----
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # only show INFO and higher
console_handler.setFormatter(formatter)


# ---- Daily Rotating File Handler ----
file_handler = TimedRotatingFileHandler(
    filename="agent.log",
    when="midnight",     # rotate at 00:00
    interval=1,          # each day
    backupCount=7,       # keep 7 days for old logs
    encoding="utf-8"
)

file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Suffix for old file log
file_handler.suffix = "%Y-%m-%d"


# ---- Add handler in logger ----
logger.addHandler(console_handler)
logger.addHandler(file_handler)
# ===================================