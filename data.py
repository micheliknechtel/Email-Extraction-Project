import json

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)
    
    def __repr__(self):
        return self.toJson()

class Email(JsonSerializable):
    def __init__(self,email,email_id):
        self.email_id = email_id
        self.email = email
