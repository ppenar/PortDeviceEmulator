'''
Created on Mar 16, 2015

@author: pawelpq
'''
import _winreg as winreg
import itertools
""" 
Code by: http://eli.thegreenplace.net/2009/07/31/listing-all-serial-ports-on-windows-with-python
"""
def enumerate_serial_ports():
    """ Uses the Win32 registry to return an
        iterator of serial (COM) ports
        existing on this computer.
    """
    path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
   
    for i in itertools.count():
        try:
            val = winreg.EnumValue(key, i)
            yield str(val[1])
        except EnvironmentError:
            break