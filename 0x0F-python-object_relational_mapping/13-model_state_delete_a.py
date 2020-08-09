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
    delete = session.query(State).order_by(State.id).all()
    for row in delete:
        if 'a' in row.name:
            session.delete(row)
    session.commit()
    session.close()
