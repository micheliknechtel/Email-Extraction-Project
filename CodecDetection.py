#  CodecDetection.py
#  python
#
#  Created by Micheli Knechtel on 05/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.
# 
#   1) Description: class CodecDetection() 
#   Enconding file detection  
 
import chardet

class CodecDetection():
#   for a given file return encoding 
    def getCodec(self,path):
        rawData = open(path,'rb').read()
        result = chardet.detect(rawData)
        return result['encoding']
