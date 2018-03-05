#  PrintManager.py
#  python
#
#  Created by Micheli Knechtel on 05/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.
# 
#   Description: class PrintManager() 
#   All content to be printed is located inside of this class


class PrintManager():
    def parse(self,fileName):
        print("-------------------------------------------")
        print("Email = "+fileName+" extracted successfully")
        print("-------------------------------------------")
    
    def nslookupTry(self, string):
        print("-------------------------------------------")
        print(string)
            
    def nslookupExcept(self, string):
       print("-------------------------------------------")
       print(string + " query failed")
       
    def missingRepository(self, path):
       print("Missing directory " + path)
       print("Shutting down the module")
