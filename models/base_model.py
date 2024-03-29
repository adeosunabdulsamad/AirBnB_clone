#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
     def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    if key != '__class__':
                            setattr(self, key, value)
        else:
                self.id = str(uuid.uuid1())
                self.created_at = datetime.datetime.now()
                self.updated_at = datetime.datetime.now()
                storage.new(self)

     def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
     def save(self):
        from models import storage 
        storage.save()

     def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
