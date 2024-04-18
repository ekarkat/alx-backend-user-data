#!/usr/bin/env python3
""" Basic Auth class """
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
import base64
from models.user import User


class SessionAuth(Auth):
    """ Class Basic Auth"""
    pass
