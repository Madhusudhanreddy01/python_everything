import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import armstrong

class Testarm(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(armstrong.arm_("153"),"Armstrong Number")
    def testcase2(self):
        self.assertEqual(armstrong.arm_("121"),"Not an Armstrong Number")


if __name__=="__main__":
    unittest.main()
