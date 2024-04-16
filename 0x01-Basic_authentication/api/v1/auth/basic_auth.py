#!/usr/bin/env python3
""" Basic Auth class """
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self, b64_auth_head: str) -> str:
        """ Encode """
        b64 = b64_auth_head
        if not b64 or not isinstance(b64, str):
            return None

        try:
            decoded_bytes = base64.b64decode(b64)
            decoded_string = decoded_bytes.decode('utf-8')
            return(decoded_string)
        except Exception:
            return None

    def extract_user_credentials(self, d_b64: str) -> (str, str):
        """ Extract """
        if d_b64 is None or not isinstance(d_b64, str) or ':' not in d_b64:
            return (None, None)
        return d_b64.split(':', 1)
