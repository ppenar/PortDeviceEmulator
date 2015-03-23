import json
from FileStatus import FileStatus

class ConfTool(object):
    '''
    classdocs
    '''


    def __init__(self, fileName):
        self.fileStatus = FileStatus.OPENERROR
        try:
            file = open(fileName)
            self.data = json.load(file)
        except IOError:
            self.fileStatus = FileStatus.OPENERROR
        else:
            self.fileStatus = FileStatus.ISOPEN
            file.close()
        '''
        Constructor
        '''
        
    def getIdNumber(self):
        return int(self.data['idNumber'])