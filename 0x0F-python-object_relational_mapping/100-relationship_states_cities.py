#!/usr/bin/python3
"""
Write a script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name="San Francisco", states=State(name="California")))
    session.commit()
    session.close()
