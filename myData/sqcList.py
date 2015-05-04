'''
Created on May 4, 2015

@author: rgao

this is mmodule of sequence list
'''

class sqcList(object):
    '''
    sequence list
    '''

    def __init__(self):
        self.data = []
        
    def clear(self):
        del self.data
        self.data = []
        
    
    def empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def length(self):
        return len(self.data)
    
    def get(self, index):
        if(index >= len(self.data)):
            return None
        return self.data[index]

    def find(self, elem):
        try:
            i = self.data.index(elem, )
            return i
        except Exception:
            return None
    
    def before(self, cur):
        pass
    
    def next(self, cur):
        pass
    
    def insert(self, index, elem):
        if(index > len(self.data)):
            return False
        self.data.insert(index, elem)
        return True
    
    def delete(self, index):
        if(index >= len(self.data)):
            return False
        self.data[index:-1] = self.data[index+1:]
        self.data.pop()
        return True
    
    