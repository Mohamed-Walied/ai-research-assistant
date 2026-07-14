import logging

from src.core import get_logger


def test_logger_is_logger():
    logger = get_logger(__name__)

    assert isinstance(logger, logging.Logger)


def test_logger_name():
    logger = get_logger("test")

    assert logger.name == "test"git add .