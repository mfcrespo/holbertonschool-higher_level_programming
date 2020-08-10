#!/usr/bin/python3
"""
Write a python file that contains the class definition
of a city:
- inherits from Base (imported from model_state)
- links to the MySQL table cities
- class attribute id that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key
- class attribute name that represents a column of a string of
128 characters and can’t be null
- class attribute state_id that represents a column of an integer,
can’t be null and is a foreign key to states.id
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """class definition of a State inherits from Base,
        links to the MySQL table cities
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
