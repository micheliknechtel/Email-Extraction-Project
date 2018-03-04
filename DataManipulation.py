import sys
from Extractor import Extractor
from Repository import Repository
from Nslookup import Nslookup
from os import path
import os

pathOutput = os.getcwd() + "/json/"
pathInput = os.getcwd() + "/email/"

Repository().checkRepositoryExist(pathInput)
Repository().checkRepositoryExist(pathOutput)


e = Extractor(pathInput, pathOutput)
Nslookup().DNSquery(e.getTopTenList(10))

