#!/usr/bin/python3
""" Module that contains the class definition of a State
and an instance Base = declarative_base() """
from sqlalchemy import Integer  # used for integer columns
from sqlalchemy import Column  # used to create columns
from sqlalchemy import String  # defines string columns
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Method" Initialize class State that inherits from Base """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    