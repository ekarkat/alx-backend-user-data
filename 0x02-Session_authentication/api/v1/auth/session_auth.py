#!/usr/bin/env python3
""" Basic Auth class """
from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
import base64
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ Class Basic Auth"""
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
