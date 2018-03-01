import chardet

class CodecDetection():
    def getCodec(self,fileName):
        rawData = open(fileName,'rb').read()
        result = chardet.detect(rawData)
        return result['encoding']
