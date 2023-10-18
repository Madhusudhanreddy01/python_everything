import sys
sys.path.append("D:\python")

import unittest
import prime_numbers

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(prime_numbers.lists(1),"Not a prime number")
    def testcase1(self):
        self.assertEqual(prime_numbers.lists(10),[2, 3, 5, 7])


if __name__=="__main__":
    unittest.main()
