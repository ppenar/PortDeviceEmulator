'''
Created on Mar 16, 2015

@author: pawelpq
'''
import serial
from PortStatus import PortStatus
from serial.serialutil import SerialException
import threading
class PortTool(object):
    '''
    classdocs
    '''


    def __init__(self,pName,statusManager):
        self.port=None;
        self.statusManager = statusManager
        self.lock = threading.Lock()
        self.portName=pName
        
    def portOpen(self):
        try:
            self.port = serial.Serial(self.portName,9600)
            self.readT = threading.Thread(target=self.readPort)
            self.readT.start()
            return PortStatus.OPEN
        except SerialException, e:
            self.portError=e
            return PortStatus.ERROR
    
    def portClose(self):
        self.port.close()
    
    def readPort(self):
        while True:
            self.lock.acquire()
            data= self.port.read()
            self.lock.release() 
            self.statusManager.readData(data,self)
    
    def writePort(self,data):
        self.lock.acquire()
        self.port.write(data)
        self.lock.release()