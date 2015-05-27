'''
Created on May 4, 2015

@author: rgao
'''
import unittest
import sqcList


class Test(unittest.TestCase):


    def setUp(self):
        self.l = sqcList.sqcList()


    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.l.length(), 0)
        t = sqcList.sqcList((1,2,3,4))
        self.assertEqual(t.length(), 4)
        for i in range(4):
            self.assertEqual(t.get(i), i+1)
        
    def test_clear(self):
        self.l.insert(0, 1)
        self.l.clear()
        self.assertTrue(self.l.empty())
    
    def test_empty(self):
        self.assertTrue(self.l.empty())
        self.l.insert(0,1)
        self.assertFalse(self.l.empty())
        self.l.clear()
        self.assertTrue(self.l.empty())
    
    def test_length(self):
        self.assertEqual(self.l.length(), 0)
        self.l.insert(0,1)
        self.assertEqual(self.l.length(), 1)
    
    def test_get(self):
        self.l.insert(0, 0)
        self.l.insert(1, 1)
        self.l.insert(2, 2)
        self.l.insert(3, 3)
        self.l.insert(4, "hello")
        self.assertEqual(self.l.get(0), 0)
        self.assertEqual(self.l.get(4), "hello")
        self.assertEqual(self.l.get(2), 2)
        self.assertEqual(self.l.get(5), None)
        self.l.delete(2)
        self.assertEqual(self.l.get(3), "hello")
        self.assertEqual(self.l.get(1), 1)
        

    def test_find(self):
        self.l.insert(0, 0)
        self.l.insert(1, 1)
        self.l.insert(2, 2)
        self.l.insert(3, 3)
        self.l.insert(4, "hello")
        self.assertEqual(self.l.find("world"), None)
        self.assertEqual(self.l.find(0), 0)
        self.assertEqual(self.l.find(1), 1)
        self.assertEqual(self.l.find(2), 2)
        self.assertEqual(self.l.find(3), 3)
        
        self.l.insert(0, 3)
        self.assertEqual(self.l.find(3), 0)
        self.assertEqual(self.l.find(4), None)
    
    def test_before(self):
        pass
    
    def test_next(self):
        pass
    
    def test_insert(self):
        self.assertEqual(self.l.length(), 0)
        self.assertFalse(self.l.insert(1, "gao"))
        self.assertEqual(self.l.length(), 0)
        
        self.assertTrue(self.l.insert(0, "gao"))
        self.assertEqual(self.l.length(), 1)
        self.assertEqual(self.l.get(0), "gao")
        
        self.assertTrue(self.l.insert(1, "zhi"))
        self.assertEqual(self.l.length(), 2)
        self.assertEqual(self.l.get(0), "gao")
        
        self.assertTrue(self.l.insert(0, 100))
        self.assertEqual(self.l.length(), 3)
        self.assertEqual(self.l.get(0), 100)
        self.assertEqual(self.l.get(1), "gao")
        self.assertEqual(self.l.get(2), "zhi")
        
        self.assertFalse(self.l.insert(4, "gao"))
    
    def test_delete(self):
        self.l.insert(0, 0)
        self.l.insert(1, 1)
        self.l.insert(2, 2)
        self.l.insert(3, 3)
        self.assertEqual(self.l.length(), 4)
        self.assertFalse(self.l.delete(4))
        
        self.assertTrue(self.l.delete(2))
        self.assertEqual(self.l.length(), 3)
        self.assertEqual(self.l.get(0), 0)
        self.assertEqual(self.l.get(1), 1)
        self.assertEqual(self.l.get(2), 3)
        
        self.assertTrue(self.l.delete(0))
        self.assertEqual(self.l.get(0), 1)
        self.assertEqual(self.l.get(1), 3)

    def test_union(self):
        self.l.insert(0, 0)
        self.l.insert(1, 1)
        self.l.insert(2, 2)
        self.l.insert(3, 3)
        tl = sqcList.sqcList()
        tl.insert(0, 0)
        tl.insert(1, 2)
        tl.insert(2, 5)
        tl.insert(3, 7)
        self.l.union(tl)
        self.assertEqual(self.l.length(), 6)
        self.assertEqual(self.l.get(0), 0)
        self.assertEqual(self.l.get(1), 1)
        self.assertEqual(self.l.get(2), 2)
        self.assertEqual(self.l.get(3), 3)
        self.assertEqual(self.l.get(4), 5)
        self.assertEqual(self.l.get(5), 7)
        
        del tl
        tl = sqcList.sqcList()
        self.l.union(tl)
        self.assertEqual(self.l.length(), 6)
        
        del tl
        tl = 1
        self.l.union(tl)
        self.assertEqual(self.l.length(), 6)

    def test_merge(self):
        self.l.insert(0, 0)
        self.l.insert(1, 3)
        self.l.insert(2, 6)
        self.l.insert(3, 8)
        tl = sqcList.sqcList()
        tl.insert(0, 0)
        tl.insert(1, 2)
        tl.insert(2, 5)
        tl.insert(3, 7)
        self.assertEqual(self.l.merge(tl), [0,0,2,3,5,6,7,8])
        self.assertEqual(self.l.merge(None), None)
        tl.clear()
        self.assertEqual(self.l.merge(tl), [0,3,6,8])
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()