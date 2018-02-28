import os
import sys
import re
import chardet
import tld
import tldextract

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
        array.append(str(matches))
#----------------------------------------------------------------------------
# execute regex for a given pattern, and if found a match add it to a given the structure
#----------------------------------------------------------------------------
def regexUrlsDomain(line, pattern, urls, topLevelDomain):
    matches = re.findall(pattern, line)
    if matches:
        array.append(str(matches))
        token = str(matches).split('http://')[1].split('/')[0]
#        topLevelDomain.append(token.split('.')[-2]+'.'+token.split('.')[-1])

#----------------------------------------------------------------------------
# check if the directory exist
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
            regex(line, patternEmail, email)
            regex(line, patternUrl, urls)
            if TO in line:
                regex(line, patternReceiver, receiver)
            if FROM in line:
                regex(line, patternSender, sender)
    file.close()

#----------------------------------------------------------------------------
# for a given file returns the codec
#----------------------------------------------------------------------------
def codecDetection(fileName):
    rawData = open(fileName,'rb').read()
    result = chardet.detect(rawData)
    print(fileName)
    print(result)
    return result['encoding']

#----------------------------------------------------------------------------
# check if the directory exist
#----------------------------------------------------------------------------
def parsingFiles(listFiles, sender, receiver, email, urls, topLevelDomain):
    for fileName in listFiles:
        parse(fileName, codecDetection(fileName), sender, receiver, email, urls, topLevelDomain)
        break

direct = "/Users/micheliknechtel/Documents/xCode/ivizone/ivizone/email"

sender   = []
receiver = []
email    = []
urls     = []
topLevelDomain = []

if repository(direct):
    parsingFiles(listOpenFiles(direct), sender, receiver, email, urls, topLevelDomain)

f = tldextract.extract(urls[0])
my_string = urls[0]
print(f)


