#!/usr/bin/python3
"""
a module that contains the entery point of the command interpreter
"""


import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """
    Enrty point to the interpreter
    """
    prompt = '(hbnb) '
    available_classes = {'User', 'BaseModel'}

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """EOF command to exit program using Ctrl D"""

        return True

    def help_all(self):
        """displays help"""
        topics = [
                "",
                "Documented commands (type help <topic>):",
                "========================================",
                "EOF  help  quit",
                ]
        for topic in topics:
            print(topic)
        print()

    def do_help(self, arg):
        """list available command with help & detail"""
        if arg == '':
            self.help_all()
        else:
            super().do_help(arg)
            print()

    def emptyline(self):

        """emptyline + ENTER won't execute anything"""

        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,saves it (JSON file) &
        prints the id

        """
        cmnd = self.parseline(arg)[0]

        if cmnd is None or cmnd == "":
            print("**class name missing**")
        elif cmnd not in self.available_classes:
            print("**class doesn't exist**")
        else:
            new = eval(cmnd + "()")
            new.save()
            models.storage.new(new)
            print(new.id)

    def do_show(self, arg):
        """
        Prints string representation of an instance based on the class
        name & id

        """
        class_name = self.parseline(arg)[0]
        obj_id = self.parseline(arg)[1]

        if class_name is None or class_name == "":
            print("** class name missing **")
        elif class_name not in self.available_classes:
            print("** class doesn't exist **")
        elif obj_id == '':
            print("** instance id missing **")
        else:
            new_obj = models.storage.all().get(class_name + '.' + obj_id)
            if new_obj is None:
                print('** no instance found **')
            else:
                print(new_obj)

    def do_destroy(self, arg):
        """
        Deletes an instance based on classname & id(save change inJSON file)

        """
        obj_id = self.parseline(arg)[1]
        class_name = self.parseline(arg)[0]

        if class_name is None or class_name == "":
            print("** class name missing **")
        elif class_name not in self.available_classes:
            print("** class doesn't exist **")
        elif obj_id == "":
            print("** instance id missing **")
        else:
            key = class_name + '.' + obj_id
            obj_data = models.storage.all().get(key)
            if obj_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string rep of all instances based /not on the class name

        """
        objects = models.storage.all()
        class_name = self.parseline(arg)[0]
        if class_name is None:
            print([str(obj) for obj in objects])
        elif class_name in self.available_classes:
            keys = objects.keys()
            print([str(objects[key]) for key in keys if key.startswith(class_name)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates instance based on class name & id by adding /updating attribute
        (save change into JSON file).
         """
        args = shlex.split(arg)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
                if args_size == 2:
                    print('** attribute name missing **')
                elif args_size == 3:
                    print('** value missing **')
                else:
                    args[3] = self.analyze_parameter_value(args[3])
                    try:
                        setattr(inst_data, args[2], args[3])
                        setattr(inst_data, 'updated_at', datetime.now())
                    except AttributeError:
                        pass
                    models.storage.save()

    def analyze_parameter_value(self, value):
        """
        analyses if a string shld be converted to float/ int
        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()
