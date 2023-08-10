#!/usr/bin/python3
"""
file storage module
"""
import json


class FileStorage:
    """
    serialises instances to a json file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        :return:"__objects"
        """
        return __objects

    def new(self,obj):
        """
        sets in the dictionary "__objects"
        "obj" as a value and <obj class name>.id
        as key
        """
        class_name = self.__class__.__name__
        key = "{}{}{}".format(class_name, '.', self.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serialises the python dictionary __objects to
        the JSON file (path:__file_path)
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(File_Storage.__objects, file)

    def reload(self):
        """
        deserialises the JSON file to
        "--objects"
        """
        if FileStorage.__file_path != None:
            try:
                with open(FileStorage.__filepath, "w", encoding="utf-8") as file:
                    FileStorage.__objects = json.load(file)
            except Exception:
                return
        return
