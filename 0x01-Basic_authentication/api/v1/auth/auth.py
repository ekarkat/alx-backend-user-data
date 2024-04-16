#!/usr/bin/env python3
""" Auth class """
from typing import List, TypeVar
from flask import request


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Documentation for method """
        return False

    def authorization_header(self, request=None) -> str:
        """ Documentation for method """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Documentation for method """
        return None
