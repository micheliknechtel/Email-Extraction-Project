import json
class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)
    
    def __repr__(self):
        return self.toJson()

class SerialiseData(JsonSerializable):
    def __init__(self,data):
        self.data = data
    
    def writeIntoFile(self, path):
        file = open(path + str(self.data["email_id"]), "w")
        file.write(self.toJson())
        file.close()
