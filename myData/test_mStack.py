'''
Created on June 3

@author: raistlin
'''
import unittest
import mStack


class Test_mStack(unittest.TestCase):


    def setUp(self):
        self.s = mStack.mStack()


    def tearDown(self):
        del self.s


    def test_clear(self):
        s = self.s
        s.clear()
        self.assertEqual(s.isEmpty(), True)
        s.push(1)
        self.assertEqual(s.isEmpty(), False)
        s.clear()
        self.assertEqual(s.isEmpty(), True)
    
    def test_isEmpty(self):
        s = self.s
        self.assertEqual(s.isEmpty(), True)
        s.push(1)
        self.assertEqual(s.isEmpty(), False)
        s.pop()
        self.assertEqual(s.isEmpty(), True)
        s.push(1)
        s.push(1)
        self.assertEqual(s.isEmpty(), False)
        s.clear()
        self.assertEqual(s.isEmpty(), True)
    
    def test_length(self):
        s = self.s
        self.assertEqual(s.length(), 0)
        s.push(1)
        self.assertEqual(s.length(), 1)
        s.push(1)
        self.assertEqual(s.length(), 2)
        s.push(1)
        self.assertEqual(s.length(), 3)
        s.pop()
        self.assertEqual(s.length(), 2)
        s.clear()
        self.assertEqual(s.length(), 0)
    
    def test_get(self):
        s = self.s
        self.assertEqual(s.get(), None)
        s.push(1)
        self.assertEqual(s.get(), 1)
        s.push("hello")
        self.assertEqual(s.get(), "hello")
        self.assertEqual(s.get(), "hello")
        s.pop()
        self.assertEqual(s.get(), 1)
        s.clear()
        self.assertEqual(s.get(), None)
    
    def test_push(self):
        s = self.s
        self.assertEqual(s.get(), None)
        s.push(1)
        self.assertEqual(s.get(), 1)
        self.assertEqual(s.length(), 1)
        s.push("hello")
        self.assertEqual(s.get(), "hello")
        self.assertEqual(s.length(), 2)
        s.push(103)
        self.assertEqual(s.get(), 103)
        self.assertEqual(s.length(), 3)
        s.push(None)
        self.assertEqual(s.get(), 103)
        self.assertEqual(s.length(), 3)
        s.clear()
        for i in range(100):
            s.push(i)
            self.assertEqual(s.get(), i)
            self.assertEqual(s.length(), i+1)
            
    
    def test_pop(self):
        s = self.s
        self.assertEqual(s.pop(), None)
        s.push(1)
        s.push("hello")
        self.assertEqual(s.pop(), "hello")
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), None)
        for i in range(100):
            s.push(i)
        for i in range(100):
            self.assertEqual(s.pop(), 99-i)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()