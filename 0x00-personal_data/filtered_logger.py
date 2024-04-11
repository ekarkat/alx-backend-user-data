#!/usr/bin/env python3
"""DOCUMENTATIONs"""

import re
import typing
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Hide infos"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
