#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    reviews = relationship('Review', cascade='all, delete', backref='Place')
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    @property
    def reviews(self):
        """Returns the list of review instances with stuff equals to
        the current stuff
        """
        from models.engine.file_storage import FileStorage
        fs = FileStorage.all(Review)
        review_list = []
        for key, value in fs.items():
            if Place.id == value.place_id:
                '''Append City instances maybe fucked up here!!!'''
                review_list.append[value]
        return review_list
