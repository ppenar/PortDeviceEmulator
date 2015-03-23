'''
Created on Mar 16, 2015

@author: pawelpq
'''
import sys, os
from PyQt4 import QtCore, QtGui
from ClassPortDeviceEmulator import Ui_Form
import listPorts
from PortTool import PortTool
from PortStatus import PortStatus
from ConfTool import ConfTool
from pylint.utils import FileState
from FileStatus import FileStatus
from time import sleep
from StateManager import StateManager
class PdeForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form();
        self.port = None;
        self.ui.setupUi(self)
        
        self.conf = ConfTool("conf.json")
        if self.conf.fileStatus== FileStatus.ISOPEN:
            self.addTextToBox("Config file: LOAD")
            self.ui.labelID.setText(str(self.conf.getIdNumber()))
        else:
            self.addTextToBox("Config file: ERROR")
            
        for portName in listPorts.enumerate_serial_ports():
            self.ui.portComboBox.addItem(portName)
        
        QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"),self.startButtonClicked)
        QtCore.QObject.connect(self.ui.resetButton,QtCore.SIGNAL("clicked()"),self.resetButtonClicked)
        QtCore.QObject.connect(self.ui.aboutButton,QtCore.SIGNAL("clicked()"),self.aboutClicked)
        self.ui.resetButton.setEnabled(False)

    def startButtonClicked(self):
        
        self.stateManager = StateManager(self.conf,self)
        self.stateManager.updateText.connect(self.updateTextBox)
        self.port = PortTool(str(self.ui.portComboBox.currentText()),self.stateManager)
        status=self.port.portOpen()
        if status==PortStatus.OPEN:
            self.addTextToBox("Port "+self.ui.portComboBox.currentText()+" is open")
            self.ui.resetButton.setEnabled(True)
        else:
            self.ui.boxTextEdit.setText("Port "+self.ui.portComboBox.currentText()+": error")
    
    def resetButtonClicked(self):
        self.ui.boxTextEdit.clear()
        self.addTextToBox("Port "+self.ui.portComboBox.currentText()+" is open")
        self.addTextToBox("----> Reset <----")
        self.stateManager.reset()
    def updateTextBox(self,text):
        self.addTextToBox(text)
    def addTextToBox(self,newText):
        oldText = self.ui.boxTextEdit.toPlainText()
        self.ui.boxTextEdit.setText(newText+"\n"+oldText)
    
    def aboutClicked(self):
        QtGui.QMessageBox.information(self, "About", "Serial Device Emulator\n Autor: P.Penar [ppenar[at]prz.edu.pl]")
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    pdeApp = PdeForm();
    pdeApp.show()
    os._exit(app.exec_())