'''
Created on Mar 23, 2015

@author: pawelpq
'''
from json import dumps, load
if __name__ == '__main__':
    f = open("test.json","wb")
    n=5
    f.write(dumps({'numbers':n}, f))