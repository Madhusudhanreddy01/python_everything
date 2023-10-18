import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import perfectnumber

class Testpri(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(perfectnumber.perfect(6), "Perfect Number")
    def testcase2(self):
        self.assertEqual(perfectnumber.perfect(12), "Not a Perfect Number")


if __name__=="__main__":
    unittest.main()