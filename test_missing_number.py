import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import missing_number

class Testmissing(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(missing_number.findMissing([17,19,18,18,21,23]), [20,22])
    def testcase2(self):
        self.assertEqual(missing_number.findMissing([2,3,5,6,8]), [4,7])


if __name__=="__main__":
    unittest.main()
