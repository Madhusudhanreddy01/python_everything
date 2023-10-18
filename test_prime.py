import sys
sys.path.append("D:\python")

import unittest
import Checking_given_number_prime

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(Checking_given_number_prime.check(3),True)
    def testcase2(self):
        self.assertEqual(Checking_given_number_prime.check(4),False)


if __name__=="__main__":
    unittest.main()
