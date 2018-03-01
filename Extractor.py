import re
from re import finditer
import tld
import tldextract
import sys
from SerialiseData import SerialiseData
from CodecDetection import CodecDetection
from Repository import Repository
from utilities import Definition
from utilities import Pattern

class Extractor():
    def __init__(self,pathInput, pathOutput):
        self.pathInput  = pathInput
        self.pathOutput = pathOutput

    def extractingFiles(self):
        r = Repository()
        c = CodecDetection()
        for fileName in r.getListOfFiles(self.pathInput):
            self.parse(fileName, c.getCodec(self.pathInput + fileName))

    def regex(self, line, pattern):
        array = []
        for match in finditer(pattern, line):
            array.append(match.group().strip('"'))
        return array
            
    def getDomains(self, urls):
        domains = []
        for i in range(len(urls)):
            domains.append(tldextract.extract(urls[i]).domain)
        return domains

    def parse(self, fileName, codec):
        location  = self.pathInput + fileName
        fileContent = ""
        receivers = []
        
        with open(location, 'rt', encoding=codec) as file:
            lines = file.read().splitlines()
            for i in range(len(lines)):
                line = lines[i]
                if Definition.FROM in line:
                    sender = {"name":str(self.regex(line, Pattern.Name)), "email":str(self.regex(line, Pattern.Email))}
                if Definition.TO  in line:
                    receivers.append({"name":str(self.regex(line, Pattern.Name)),"email":str(self.regex(line, Pattern.Email))})
                fileContent = fileContent + lines[i]
            urls = (self.regex(fileContent, Pattern.Url))
            email = (self.regex(fileContent, Pattern.Email))
        file.close()
        domains = self.getDomains(urls)
        data = {"email_id":int(fileName), "email":email, "domains":domains, "sender":sender, "receivers":receivers}
        SerialiseData(data).writeIntoFile(self.pathOutput)


