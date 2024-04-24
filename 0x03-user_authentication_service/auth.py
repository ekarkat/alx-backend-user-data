#!/usr/bin/env python3

"""Auth Module"""
import bcrypt
from db import DB
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """Hash a password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """Generate a UUID string"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a User"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists.".format(email))
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            new_user = self._db.add_user(email, hashed_pwd)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate usr login"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """ Generate a session id """
        try:
            user = self._db.find_user_by(email=email)
            ses_id = _generate_uuid()
            self._db.update_user(user.id, session_id=ses_id)
            return ses_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """ Get user by session id """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user.email
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destry session"""
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Rest password tokker"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
