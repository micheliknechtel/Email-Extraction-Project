import json
from typing import NamedTuple

class Data(NamedTuple):
    email_id:  int
    email:     list
    domains:   list
    sender:    list
    receivers: list

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)
    
    def __repr__(self):
        return self.toJson()

class SerialiseDataStructure(JsonSerializable):
    def __init__(self,data):
        self.dataStructure = data
