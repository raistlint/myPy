'''
Created on Jun 2, 2015

@author: rgao
'''

class downloadManageError(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg
        
class downloadManage(object):
    '''
    this class is help to down load image or other file from url list
    usage: 
        create class content
        setUrl()
        run()
        wait until isDone()
        or stop()
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__run = False
        
    def setUrl(self):
        '''
        set url list to be download
        
        note: only invoke when downloadManage is stop
        '''
        
    def appendUrl(self):
        '''
        append new url to download url list,
        this function can be invoke during the downloading is running
        '''
        
    def setPath(self):
        '''
        set save path
        if no such folder, it will create the folder
        
        note: only invoke when downloadManage is stop
        '''
        
    def setThreadNum(self):
        '''
        default thread to download is 1
        use this function to set the number of thread, which can 
        multi-thread to download the data
        
        note: only invoke when downloadManage is stop
        '''
        
    def setFmtName(self):
        '''
        set save file name format.
        the default format is "file-%03d"
        
        note: only invoke when downloadManage is stop
        '''
        
    def run(self):
        '''
        start work of downloadManage
        '''
        
    def isDone(self):
        '''
        return the current work status of downloadManage
        
        return:
            True - downloadManage is running
            False - downloadManage is stop
        '''
        
    def stop(self):
        '''
        force to stop the download job.
        '''
    
    # private function