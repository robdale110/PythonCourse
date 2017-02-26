from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ = "Person"

    # Here we define columns for the table Person
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = "Address"

    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250))
    person_id = Column(Integer, ForeignKey("Person.id"))
    person = relationship(Person)

# Create an engine that stores the data in the local directory'set
# test_db.db file
engine = create_engine("sqlite:///test_db.db")

# Create all tables in the engine
Base.metadata.create_all(engine)
