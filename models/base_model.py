#!/usr/bin/python3
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
    it defines the attributes/methods that
    are used by other classes
    """

    def __init__(self, *args, **kwargs):
        """
        The init method,
        it serves as the class constructor
        """
        if (len(kwargs) != 0) or (len(kwargs)) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    kwargs[key] = datetime.strftime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    del kwargs["__class__"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        String method for formating string outputs
        :return: the formatted string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        function that updates public instance attribute
        'self.updated_at' with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        converts all attributes of a class instance to
        to dictionaru, including the class name
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
