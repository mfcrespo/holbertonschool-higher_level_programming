#!/usr/bin/python3
"""
Write a script that that prints all City objects from the database
"""

from sys import argv
from model_state import Base, State
from model_city import City
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
    for states, cities in session.query(State, City).order_by(City.id)\
            .filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
