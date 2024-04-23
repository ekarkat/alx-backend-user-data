#!/usr/bin/env python3

"""Auth Module"""
import bcrypt


def _hash_password(password: str) -> str:
    """Hash a password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
