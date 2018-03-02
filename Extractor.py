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
        if  not array:
            array.append(" ")
        return array

    def getDomains(self, urls):
        domains = []
        for i in range(len(urls)):
            subdomain = tldextract.extract(urls[i]).subdomain
            domain    = tldextract.extract(urls[i]).domain[0:3]
            suffix    = tldextract.extract(urls[i]).suffix
            if not subdomain:
                domains.append(domain + "." + suffix)
            else:
                domains.append(subdomain+ "." +domain + "." + suffix)
    
        return domains

    def parse(self, fileName, codec):
        location  = self.pathInput + fileName
        fileContent = ""
        receivers = []
        sender = {}
        with open(location, 'rt', encoding=codec) as file:
            lines = file.read().splitlines()
            for i in range(len(lines)):
                auxLine = lines[i]
                line = lines[i].strip("=")
                if Definition.FROM in line:
                    sender = {"name":self.regex(line, Pattern.Name)[0], "email":self.regex(line, Pattern.Email)[0]}
                if Definition.TO  in line:
                    receivers.append({"name":self.regex(line, Pattern.Name)[0],"email":self.regex(line, Pattern.Email)[0]})
                fileContent = fileContent + line

        file.close()
        urls = (self.regex(fileContent, Pattern.Url))
        email = (self.regex(fileContent, Pattern.Email))
        domains = self.getDomains(urls)
        
        data = {"email_id":int(fileName), "email":email, "domains":domains, "sender":sender, "receivers":receivers}
        SerialiseData(data).writeIntoFile(self.pathOutput)

        for i in range(len(urls)):
            print(domains[i])
        
        print("------------------------")
        print(fileName)
        print("------------------------")

        if fileName == "28":
            SerialiseData(data).writeIntoFile(self.pathOutput)
            for i in range(len(urls)):
                print(urls[i])
                print(domains[i])
            sys.exit()
