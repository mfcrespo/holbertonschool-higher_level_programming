#!/usr/bin/python3
"""
Write a script that changes the name of a State object from the database
"""

from sys import argv
from model_state import Base, State
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
    new_state = session.query(State).filter_by(id=2).first()
    new_state.name = 'New Mexico'
    session.add(new_state)
    session.commit()
    session.close()
