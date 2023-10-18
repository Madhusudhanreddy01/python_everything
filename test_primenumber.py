import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import primenumber

class Testpri(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(primenumber.prime_(29), "Prime Number")
    def testcase2(self):
        self.assertEqual(primenumber.prime_(28), "Not a Prime Number")


if __name__=="__main__":
    unittest.main()
