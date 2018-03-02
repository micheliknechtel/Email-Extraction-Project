import sys
from Extractor import Extractor
from Repository import Repository


pathInput  = "/Users/micheliknechtel/Documents/xCode/ivizone/Email-Extraction-Project/email2/"
pathOutput = "/Users/micheliknechtel/Documents/xCode/ivizone/Email-Extraction-Project/json/"

Repository().checkRepositoryExist(pathInput)
Repository().checkRepositoryExist(pathOutput)

print(pathInput[0:3])
Extractor(pathInput, pathOutput).extractingFiles()



