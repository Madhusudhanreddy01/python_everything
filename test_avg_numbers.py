import sys
sys.path.append("D:\python")

import unittest
import average_of_numbers

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(average_of_numbers.lst([1,2,3,4,5]),3.0)
    def testcase2(self):
        self.assertEqual(average_of_numbers.lst([7,8,9,0,8]),6.4)


if __name__=="__main__":
    unittest.main()
