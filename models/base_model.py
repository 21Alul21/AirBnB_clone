#!/usr/bin/pyhon3

"""
This module contains the class "BaseModel"
that defines all common attributes/methods 
for other classes in this project
"""

from datetime import datetime
import uuid



class BaseModel:
    """
    This is the base class,
    it defines the attributes/methods 
    that are used by other classes
    """
    
    def __ini__(self, *args, **kwargs):
        """
        The init method which 
        serves as a constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Method that updates public
        intance attributes 'self.updated_at'
        with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        converts all attributes of a class instance
        to dictionary, including the class itself
        """
        dictionary = self.__dict__.copy
        dictionary["created_at_"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class.__name__
        return dictionary
 
