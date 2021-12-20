#!/usr/bin/python3
''' Prints the State object with the name passed as argument from the database hbtn_0e_6_usa
    It takes 4 arguments - 1st arg = user
                         - 2nd arg = passwd
                         - 3rd arg = database_name
                         - 4ht arg = state_name to search
'''
import sys

from sqlalchemy.sql.elements import Null
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]));
#engine = create_engine('mysql+mysqldb://root:Lilstex4good95@localhost:3306/hbtn_0e_6_usa', pool_pre_ping=True);

Session = sessionmaker(bind=engine);
session = Session();

states = session.query(State).order_by(State.id);
for state in states:
    if (state.name == sys.argv[4]):
        print('{}'.format(state.id));