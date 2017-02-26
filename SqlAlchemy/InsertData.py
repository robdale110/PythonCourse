from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Create import Address, Base, Person

engine = create_engine("sqlite:///test_db.db")
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

# DBSession communicates with DB represents a "staging zone". Any changes 
# made to objects will not be persisted until session.commit() is called
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Insert a new Person in the person table
new_person = Person(name="new Person")
session.add(new_person)
session.commit()

# Insert an Address
new_address = Address(post_code="000000", person=new_person)
session.add(new_address)
session.commit()
