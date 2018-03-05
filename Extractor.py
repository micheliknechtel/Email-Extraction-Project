#  Extractor.py
#  python
#
#  Created by Micheli Knechtel on 05/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.
# 
#   Description: class Extractor()
# 
#   Class extracts and write in a customized json schema the following
#   data from a given repository (multiple files) :
# 
#   * All email addresses 
#   * All valid top-level domains 
#   * All urls 
#   * All Sender names: 
#   * All Receiver names
# 
#   This class also rank top domains.


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
    
#   this method set-up input and output path and start the extraction process 
    def __init__(self,r):
        self.r  = r
        self.extractingFiles()
  
#   this method start the parse to a list of files in input repository
    def extractingFiles(self):
        for fileName in self.r.getListOfFiles(self.r.getInputRepository()):
            self.parse(fileName, CodecDetection().getCodec(self.r.getInputRepository() + fileName))

#   for a given (string, pattern) the method evaluate a regular
#   expression returning a list of matched occurrences
    def regex(self, line, pattern):
        list = []
        for match in finditer(pattern, line):
            list.append(match.group().strip('"'))
        if  not list:
            list.append(" ")
        return list

#   to each url "u" in urls, the method extract the domain
#   building a score list of domains
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
    
#   returns a list of top "n" domains   
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
                
#   this function parse a given file extracting the following structures:
#   email, urls, sender, receiver, domain
#   Lastly, the structures will be write in a file as json representation        
    def parse(self, fileName, codec):
        fileContent = ""
        receivers = []
        domains   = []
        urls = []
        email = []
        sender = {}
        
        with open(self.r.getInputRepository() + fileName, 'rt', encoding=codec) as file:
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
        SerialiseData(data).writeIntoFile(self.r.getOutputRepository())
        PrintManager().parse(fileName);

       

        





      


