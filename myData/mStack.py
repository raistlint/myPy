'''
Created on June 3

@author: raistlin
'''

class mStack(object):
    '''
    a class for simple stack
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__data = []
        
    def __del__(self):
        '''
        destroy
        '''
        del self.__data
    
    def clear(self):
        '''
        clear the stack
        
        no return
        '''
        del self.__data
        self.__data = []
    
    def isEmpty(self):
        '''
        check if the stack is empty
        
        return: 
            True - stack is empty
            False - stack is not empty
        '''
        if len(self.__data) == 0:
            return True
        else:
            return False
    
    def length(self):
        '''
        return the stack length
        '''
        return len(self.__data)
    
    def get(self):
        '''
        return the last value of stack
        if stack is empty, return none
        '''
        if len(self.__data) == 0:
            return None
        return self.__data[-1]
    
    def push(self, value):
        '''
        push a value to the top of stack
        
        no return
        '''
        if value == None:
            return
        self.__data.append(value)
    
    def pop(self):
        '''
        pop up the value of top item of stack and remove it
        
        return:
            the value of top item of stack
            if stack is empty, return none
        '''
        if len(self.__data) == 0:
            return None
        return self.__data.pop()