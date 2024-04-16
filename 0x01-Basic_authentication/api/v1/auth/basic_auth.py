#!/usr/bin/env python3
""" Basic Auth class """
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class Basic Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extrct base """
        at = authorization_header
        if not at or not isinstance(at, str) or not at.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]
