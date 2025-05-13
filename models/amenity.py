#!/usr/bin/python3
"""
defining amenity class, the subclass of basemodel
"""

from models.base_model import BaseModel


class State(BaseModel):
    name: str = ""
