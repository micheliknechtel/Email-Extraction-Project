import os
import sys
from os import path
class Repository():
    
    def getListOfFiles(self,path):
        files = []
        listFiles = os.listdir(path)
        listFiles.sort(key=int)
        for name in listFiles:
            if os.path.isfile(os.path.join(path, name)):
                files.append(name)
        return files

    def checkRepositoryExist(self,path):
        if not os.path.exists(path):
            print("Missing directory " + path)
            print("Shutting down the module")
            sys.exit()

