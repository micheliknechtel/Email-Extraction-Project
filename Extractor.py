import re
from re import finditer
import tld
import tldextract
import sys
from SerialiseData import SerialiseData
from CodecDetection import CodecDetection
from Repository import Repository
from Utilities import Definition
from Utilities import Pattern
from PrintManager import PrintManager

class Extractor():
    topDomains = {}
    def __init__(self,pathInput, pathOutput):
        self.pathInput  = pathInput
        self.pathOutput = pathOutput
        self.extractingFiles()
    
    def extractingFiles(self):
        r = Repository()
        for fileName in r.getListOfFiles(self.pathInput):
            self.parse(fileName, CodecDetection().getCodec(self.pathInput + fileName))
            if fileName == "1000":
                break

    def regex(self, line, pattern):
        array = []
        for match in finditer(pattern, line):
            array.append(match.group().strip('"'))
        if  not array:
            array.append(" ")
        return array

    def getDomains(self, urls):
        domains = []
        c = 0
        for i in range(len(urls)):
            subdomain = tldextract.extract(urls[i]).subdomain
            domain    = tldextract.extract(urls[i]).domain
            suffix    = tldextract.extract(urls[i]).suffix[0:3]
            if not subdomain:
                domains.append(domain + "." + suffix)
            else:
                domains.append(subdomain+ "." +domain + "." + suffix)
          
            if  self.topDomains.get(str(domains[c])):
                self.topDomains[str(domains[c])] = self.topDomains.get(str(domains[c])) + 1
            else:
                self.topDomains.update({str(domains[c]):1})
            c = c + 1
        return domains
    
    def getTopTenList(self, number):
        topList = []
        sortedItems = sorted(self.topDomains, key=self.topDomains.get , reverse = True)
        c  = 0
        for element in sortedItems :
            topList.append(element)
            c = c + 1
            if  c == number:
                return topList
        return topList
                
        
    def parse(self, fileName, codec):
        fileContent = ""
        receivers = []
        domains   = []
        urls = []
        email = []
        sender = {}
        
        with open(self.pathInput + fileName, 'rt', encoding=codec) as file:
            lines = file.read().splitlines()
            for i in range(len(lines)):
                line = lines[i].strip("=")
                line = str(line).encode('ascii', 'ignore').decode('utf-8')
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
        PrintManager().emailExtractedSuccessfully(fileName);

       

        





      


