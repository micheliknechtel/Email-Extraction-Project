import os
import sys
import re
import chardet
import tld
import tldextract
from data import Email
from typing import NamedTuple

class dataStructure(NamedTuple):
    email_id:  int
    email:     list
    domains:   list
    sender:    list
    receivers: list


#----------------------------------------------------------------------------
# returns a list of files for a given repository
#----------------------------------------------------------------------------
def listOpenFiles(path):
    files = []
    listFiles = os.listdir(path)
    listFiles.sort(key=int)
    for name in listFiles:
        if os.path.isfile(os.path.join(path, name)):
            files.append(path + "/" + name)
    return files

#----------------------------------------------------------------------------
# check if the repository exist, if not shuttdown module
#----------------------------------------------------------------------------
def repository(path):
    if not os.path.exists(path):
        print("Missing directory " + path)
        print("Shutting down the module")
        return False
    return True

#----------------------------------------------------------------------------
# execute regex for a given pattern, and if found a match add it to a given the structure
#----------------------------------------------------------------------------
def regex(line, pattern, array):
    matches = re.findall(pattern, line)
    if matches:
        array.append(matches)

#----------------------------------------------------------------------------
# Parse entire a given file filling up the structures sender, receiver, email, urls, topLevelDomain
#----------------------------------------------------------------------------
def parse(infile, codec, sender, receiver, email, urls, topLevelDomain):
    patternUrl      = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    patternSender   = 'From: \"([^\"]*)\"'
    patternReceiver = 'To: \"([^\"]*)\"'
    patternEmail    = r'[\w\.-]+@[\w\.-]+'
    FROM = "From: "
    TO   = "To: "
    with open(infile, 'rt', encoding=codec) as file:
        for line in file:
            regex(line, patternUrl, urls)
            regex(line, patternEmail, email)
            if TO in line:
                regex(line, patternReceiver, receiver)
            if FROM in line:
                regex(line, patternSender, sender)
    file.close()
    for i in range(len(urls)):
        string = ''.join(str(u) for u in urls[i])
        topLevelDomain.append(tldextract.extract(string).suffix)

#----------------------------------------------------------------------------
# for a given file returns the codec
#----------------------------------------------------------------------------
def codecDetection(fileName):
    rawData = open(fileName,'rb').read()
    result = chardet.detect(rawData)
    return result['encoding']

#----------------------------------------------------------------------------
# check if the directory exist
#----------------------------------------------------------------------------
def parsingFiles(listFiles, sender, receiver, email, urls, topLevelDomain):
    for fileName in listFiles:
        parse(fileName, codecDetection(fileName), sender, receiver, email, urls, topLevelDomain)
        break

direct = "/Users/micheliknechtel/Documents/xCode/ivizone/Email-Extraction-Project/email"

sender   = []
receiver = []
email    = []
urls     = []
topLevelDomain = []

if repository(direct):
    parsingFiles(listOpenFiles(direct), sender, receiver, email, urls, topLevelDomain)

e = Email(email, 0)
print(e.toJson())

#print(sender)
#print(receiver)
#print(email)
#print(urls)
#print(topLevelDomain)


