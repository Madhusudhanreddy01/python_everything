import sys
sys.path.append("D:\python")

import unittest
import count_vowels

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(count_vowels.string("bharath"),2)
    def testcase1(self):
        self.assertEqual(count_vowels.string("bharathkumar"),4)


if __name__=="__main__":
    unittest.main()
