import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)


def get_logger(logfile="dundie.log"):
    """Returns a configured logger."""
    # ch = logging.StreamHandler() # Console/terminal/stderr
    # ch.setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        logfile,
        maxBytes=10**6,  # max bytes padrão é 10**6, que é 1 MB
        backupCount=10,  # quantidade de arquivos salvos de backup
    )

    fh.setLevel(LOG_LEVEL)

    # ch.setFormatter(fmt)
    fh.setFormatter(fmt)
    # log.addHandler(ch)
    log.addHandler(fh)
    return log
