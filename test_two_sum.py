import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import two_sum

class Testtwo_(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(two_sum.twoSum([2,7,11,15], 9), [0,1])
    def testcase2(self):
        self.assertEqual(two_sum.twoSum([3,2,4], 6), [1,2])


if __name__=="__main__":
    unittest.main()
