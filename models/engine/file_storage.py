#!/usr/bin/python3
"""This module is the file storage class"""
import json
import os
import datetime

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        objname = obj.__class__.__name__
        objID = obj.id
        key = f"{objname}.{objID}" # <class name>.id = obj
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path)'''
        # serialize the object by first converting it to a dictionary
        file_name = self.__file_path
        if os.path.exists(file_name):
            with open(file_name, 'r+', encoding="utf-8") as my_file:
                # get json data from file & convert to dictionary object
                # object_dict = json.load(my_file)
                object_dict = json.loads(my_file.read())
        else:
            object_dict = {}

        for key in self.__objects.keys():
            if type(self.__objects[key]) != dict:
                object_dict[key] = self.__objects[key].to_dict()
        # convert the dictionary object to json and write to the file
        file_name = self.__file_path
        with open(file_name, "w", encoding="utf-8") as jsonfile:
            # json.dump(object_dict, jsonfile)
            jsonfile.write(json.dumps(object_dict))
    
    def reload(self):
        '''deserializes the JSON file to __objects'''
        file_name = self.__file_path
        if os.path.exists(file_name):
            with open(file_name, 'r+', encoding="utf-8") as my_file:
                # get json data from file & convert to dictionary object
                # object_dict = json.load(my_file)
                object_dict = json.loads(my_file.read())
                
                # delete class name from dictionary
                for id, dictionary in object_dict.items():
                    # class_name = dictionary['__class__']
                    del dictionary['__class__']
                    self.__objects[id] = dictionary
        
