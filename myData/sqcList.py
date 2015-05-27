'''
Created on May 4, 2015

@author: rgao

this is mmodule of sequence list
'''

class sqcList(object):
    '''
    sequence list
    '''

    def __init__(self, l=None):
        if l == None:
            self.data = []
        else:
            self.data = list(l)
        
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
    
    # Algo 2.1
    def union(self, lb):
        if (not isinstance(lb, sqcList)) or lb.empty():
            return
        for i in range(lb.length()):
            d = lb.get(i)
            if self.find(d) == None:
                self.insert(self.length(), d)
                
    # Algo 2.2
    def merge(self, lb):
        if not isinstance(lb, sqcList):
            return
        re = []
        i = j = 0
        while i < self.length() and j < lb.length() :
            if self.get(i) <= lb.get(j):
                re.append(self.get(i))
                i+=1
            else:
                re.append(lb.get(j))
                j+=1
        while i< self.length():
            re.append(self.get(i))
            i+=1
        while j<lb.length():
            re.append(lb.get(j))
            j+=1
        return re
    
    