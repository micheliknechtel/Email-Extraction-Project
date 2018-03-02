import sys
from Extractor import Extractor
from Repository import Repository


pathInput  = "/Users/micheliknechtel/Documents/xCode/ivizone/email2/"
pathOutput = "/Users/micheliknechtel/Documents/xCode/ivizone/json/"

Repository().checkRepositoryExist(pathInput)
Repository().checkRepositoryExist(pathOutput)

Extractor(pathInput, pathOutput).extractingFiles()



