import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=True)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    password = Column(String(250), nullable=True)
    favorite = relationship("Favorites", backref="user")

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    race = Column(String(250), nullable=True)
    height = Column(String(250), nullable=True)
    eyes_color = Column(String(250), nullable=True)
    favorite = relationship("Favorites", backref="characters")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    local = Column(String(250), nullable=True)
    dimension = Column(String(250), nullable=True)
    color = Column(String(250), nullable=True)
    favorite = relationship("Favorites", backref="planets")

class Spaceships(Base):
    __tablename__ = 'spaceships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    color = Column(String(250), nullable=True)
    guns = Column(String(250), nullable=True)
    velocity = Column(String(250), nullable=True)
    favorite = relationship("Favorites", backref="spaceships")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_fk = Column(Integer, ForeignKey("user.id"))
    characters_fk = Column(Integer, ForeignKey("characters.id"))
    planet_fk = Column(Integer, ForeignKey("planets.id"))
    spaceships_fk = Column(Integer, ForeignKey("spaceships.id"))
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
