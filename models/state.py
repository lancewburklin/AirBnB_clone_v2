#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
    if environ.get("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to
            the current State.id
            """
            from models.engine.file_storage import FileStorage
            fs = FileStorage.all(City)
            city_list = []
            for key, value in fs.items():
                if type(value) == City and self.id == value.state_id:
                    '''Append City instances maybe fucked up here!!!'''
                    city_list.append(value)
                    return city_list
