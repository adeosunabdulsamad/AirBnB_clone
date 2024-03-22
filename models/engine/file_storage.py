#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    # Dynamically import the class
                    cls_name = v['__class__']
                    self.new(eval(cls_name)(**v))
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)
            pass

