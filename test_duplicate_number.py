import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import duplicate_number

class Testduplicate(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(duplicate_number.duplicate([17,19,18,18,21]), [18])
    def testcase2(self):
        self.assertEqual(duplicate_number.duplicate([2,3,4,5,6,4,7]), [4])


if __name__=="__main__":
    unittest.main()
