#!/usr/bin/python3

"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).filter(State.
                                         name.like("%a%")).order_by(State.id):
        print("{}: {}".format(i.id, i.name))

    session.close()
