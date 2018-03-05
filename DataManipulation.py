#  DataManipulation.py
#  python
#
#  Created by Micheli Knechtel on 05/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.
# 
#   Description: holds the application flow 
#   1) set correct paths
#   2) set-up input and output repositories
#   3) start extraction
#   4) perform DNSQuery

import sys
from Extractor import Extractor
from Repository import Repository
from Nslookup import Nslookup
from os import path
import os

pathOutput = os.getcwd() + "/json/"
pathInput = os.getcwd() + "/email/"

r = Repository()
r.setInputRepository(pathInput)
r.setOutputRepository(pathOutput)

e = Extractor(r)

Nslookup().DNSquery(e.getTopTenList(10))

