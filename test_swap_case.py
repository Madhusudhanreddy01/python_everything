import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import swap_case

class Testswap(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(swap_case.modify("MADHU"), "madhu")
    def testcase2(self):
        self.assertEqual(swap_case.modify("madhu"), "MADHU")


if __name__=="__main__":
    unittest.main()