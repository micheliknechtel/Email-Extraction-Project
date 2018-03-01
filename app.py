import sys
from Extractor import Extractor
from Repository import Repository


pathInput  = "/Users/micheliknechtel/Documents/xCode/ivizone/Email-Extraction-Project/email/"
pathOutput = "/Users/micheliknechtel/Documents/xCode/ivizone/Email-Extraction-Project/json/"

Repository().checkRepositoryExist(pathInput)
Repository().checkRepositoryExist(pathOutput)
Extractor(pathInput, pathOutput).extractingFiles()



