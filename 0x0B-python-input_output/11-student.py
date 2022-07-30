#!/usr/bin/python3
"""
This module has a class Student that defines a student by first_name, last_name and age
"""

class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student"""
        if attrs is not None:
            data = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    data[k] = v
            return data
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for (k, v) in json.items():
            setattr(self, k, v)