import sys
sys.path.append("D:\python")

import unittest
import duplicates_in_string

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(duplicates_in_string.string("bharath"),['h', 'a'])
    def testcase1(self):
        self.assertEqual(duplicates_in_string.string("bharathkumar"),['h', 'a', 'r'])


if __name__=="__main__":
    unittest.main()
