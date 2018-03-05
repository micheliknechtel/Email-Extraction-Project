#  SerialiseData.py
#  python
#
#  Created by Micheli Knechtel on 05/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.
# 
#   1) Description: class JsonSerializable() 
#   This class allows to get the JSON representation of an object
# 
#   2) Description: class SerialiseData() 
#   Class designed to write and read custom json data

import json
from pprint import pprint

class JsonSerializable(object):

#   serialise obj as a JSON formatted 
    def toJson(self):
        return json.dumps(self.__dict__)
        
#   returns JSON object    
    def __repr__(self):
        return self.toJson()

class SerialiseData(JsonSerializable):
    
    def __init__(self,data):
        self.data = data
    
    def writeIntoFile(self, path):
        file = open(path + str(self.data["email_id"]), "w")
        file.write(self.toJson())
        file.close()

    def readFromFile(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
            return data
