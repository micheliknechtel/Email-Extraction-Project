#  Repository.py
#  python
#
#  Created by Micheli Knechtel on 05/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.
# 
#   Description: class Repository()
# 	Class to manage a repository, with a path representing of a given
#   repository, its possible to answer such questions:
# 
#   1) Does this repository exist ? 
#   2) Can I have a list of existing files on repository?

import os
import sys
from os import path
from PrintManager import PrintManager

class Repository():
    input = ""
    output = ""
    
		
# 	returns a list of files for a given directory    
    def getListOfFiles(self,path):
        files = []
        listFiles = os.listdir(path)
        listFiles.sort(key=int)
        for name in listFiles:
            if os.path.isfile(os.path.join(path, name)):
                files.append(name)
        return files

#   check if the repository exist
    def checkRepositoryExist(self,path):
        if not os.path.exists(path):
            PrintManager().missingRepository(path)
            sys.exit()

    def setInputRepository(self,path):
        self.checkRepositoryExist(path) 
        self.input = path

    def setOutputRepository(self,path):
        self.checkRepositoryExist(path) 
        self.output = path

    def getInputRepository(self):
        return self.input

    def getOutputRepository(self):
        return self.output