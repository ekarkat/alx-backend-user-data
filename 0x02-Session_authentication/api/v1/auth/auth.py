#!/usr/bin/env python3
""" Auth class """
from typing import List, TypeVar
from flask import request
import os


class Auth():
    """ Class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Documentation for method """
        if not excluded_paths or not path:
            return True
        if path in excluded_paths or (path + '/') in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Documentation for method """
        if request is None:
            return None
        header = request.headers.get("Authorization")
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Documentation for method """
        return None

    def session_cookie(self, request=None):
        """ Return session cockies """
        if not request:
            return None
        cockie_name = os.getenv('SESSION_NAME', "_my_session_id")
        return request.cookies.get(cockie_name)
