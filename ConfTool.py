import json
import os.path
from FileStatus import FileStatus
from json import dumps, load
from random import randint
class ConfTool(object):
    '''
    classdocs
    '''


    def __init__(self, fileName):
        self.fileStatus = FileStatus.OPENERROR
        try:
            file = open(fileName)
            
        except IOError:
            if not os.path.isfile(fileName):
                newfile= open(fileName,"wb")
                id =randint(2,12)
                newfile.write(dumps({'idNumber':id},newfile ))
                newfile.close()
                file = open(fileName)
                self.data = json.load(file)
                self.fileStatus = FileStatus.ISOPEN
            else:
                self.fileStatus = FileStatus.OPENERROR
        else:
            self.data = json.load(file)
            self.fileStatus = FileStatus.ISOPEN
            file.close()
        '''
        Constructor
        '''
        
    def getIdNumber(self):
        return int(self.data['idNumber'])