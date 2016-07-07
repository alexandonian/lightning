from . import series
from . import image
from . import resources


def _setup():
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(name)s] %(levelname)s %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)


_setup()

__version__ = '1.2.0'
