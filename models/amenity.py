#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
