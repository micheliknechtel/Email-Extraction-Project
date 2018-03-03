import sys
from Extractor import Extractor
from Repository import Repository
from Nslookup import Nslookup


pathInput  = "/Users/micheliknechtel/Documents/xCode/ivizone/email/"
pathOutput = "/Users/micheliknechtel/Documents/xCode/ivizone/json/"

Repository().checkRepositoryExist(pathInput)
Repository().checkRepositoryExist(pathOutput)

e = Extractor(pathInput, pathOutput)
Nslookup().DNSquery(e.getTopTenList(10))

