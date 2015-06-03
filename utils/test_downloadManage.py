'''
Created on Jun 3, 2015

@author: integration
'''
import unittest
import downloadManage


class Test_downloadManage(unittest.TestCase):


    def setUp(self):
        self.dl = downloadManage.downloadManage()


    def tearDown(self):
        pass


    def test_setUrl(self):
        dl = self.dl
        self.assertEqual(1, 2)
    
    def test_appendUrl(self):
        pass
    
    def test_setPath(self):
        pass
    
    def test_setThreadNum(self):
        pass
    
    def test_setFmtName(self):
        pass
    
    def test_run(self):
        pass
    
    def test_isDone(self):
        pass
    
    def test_stop(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()