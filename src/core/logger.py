import logging


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger.

    Args:
        name: Usually __name__ of the calling module.

    Returns:
        Configured logger.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger