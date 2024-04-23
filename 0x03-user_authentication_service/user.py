#!/usr/bin/python3
""" The User module """

""" The User module """

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import registry


mapper_registry = registry()


@mapper_registry.mapped
class User():
    """ The user class"""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(250), nullable=True)
    session_id: Mapped[str] = mapped_column(String(250), nullable=True)
    reset_token: Mapped[str] = mapped_column(String(250), nullable=True)
