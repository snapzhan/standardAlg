'''
Created on 2012-4-15

@author: Snap_Zhan
'''
import mysearch
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    def test_line_search(self):
        key1 = 1
        list1 = range(10)
        self.assertEqual(key1, mysearch.line_search(key1, list1))
        key2 = 10
        self.assertEqual(-1, mysearch.line_search(key2, list1))
        
    def test_line_searchp(self):
        key = 99999
        list2 = range(-10000,1000000)
        self.assertEqual(109999, mysearch.line_search(key, list2))

 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()