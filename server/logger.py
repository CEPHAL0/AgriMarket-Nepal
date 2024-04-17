import logging

logger = logging.getLogger(__name__)

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="fastapi.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)
