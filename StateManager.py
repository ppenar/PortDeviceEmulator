'''
Created on Mar 17, 2015

@author: pawelpq
'''
import random
import struct
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject
class StateManager(QtCore.QObject):
    '''
    classdocs
    '''

    updateText = QtCore.pyqtSignal(str)
    
    def __init__(self,conf,ui):
        QObject.__init__(self)
        self.gui=ui
        self.maxStep=3
        self.firstData=True
        self.sendMode=True
        self.waitMode = False
        self.diviceIsRunning = False
        self.conf = conf
        self.step = 1
       
        
    def readData(self,data,portToolHandler):
        if self.firstData == True:
            isDataOk =self.readFirstData(data,portToolHandler)
            if isDataOk:
                self.firstData=False
        
        
        
        if self.firstData==False and self.step<=self.maxStep:
            if self.waitMode == True:
                self.waitFun(data,portToolHandler)
                if (self.step-1) == self.maxStep:
                    self.diviceIsRunning=True
                    self.updateText.emit("Device running")

            if self.sendMode == True and not self.diviceIsRunning:
                self.sendFun(portToolHandler)
        
            
                    
    def readFirstData(self,data,portToolHandler):
        idCompare = self.conf.getIdNumber()*self.conf.getIdNumber()
        if idCompare == ord(data):
            self.updateText.emit("Config mode: START")
            portToolHandler.writePort("\x01")
            self.updateText.emit("Config mode: Send ACK")
            return True
        else:
            self.updateText.emit("Config mode: ERROR")
            portToolHandler.writePort("\x02")
            return False
        
        
    def waitFun(self,data,portToolHandler):
        intCompare = self.calcCompare()
        if intCompare == ord(data):
            self.updateText.emit("Config step "+str(self.step)+": Receiver: "+str(ord(data)))
            portToolHandler.writePort("\x01")
            self.updateText.emit("Config step "+str(self.step)+": Send ACK")
            self.sendMode =True
            self.step = self.step+1
            self.waitMode = False
        else: 
            portToolHandler.writePort("\x02")
            self.updateText.emit("Config mode: ERROR")
           
            
    def sendFun(self,portToolHandler):
            self.sendInt=random.randint(1,100)
            portToolHandler.writePort(struct.pack('!B',self.sendInt))
            self.updateText.emit("Config step "+str(self.step)+": Send data")
            self.sendMode =False
            self.waitMode = True
            
    
    def calcCompare(self):
        return self.sendInt*2
    
    def reset(self):
        self.maxStep=3
        self.firstData=True
        self.sendMode=True
        self.waitMode = False
        self.diviceIsRunning = False
        self.step = 1