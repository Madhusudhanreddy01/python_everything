import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import palindrome_number

class Testpalin(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(palindrome_number.isPalindrome(121), True)
    def testcase2(self):
        self.assertFalse(palindrome_number.isPalindrome(122), False)


if __name__=="__main__":
    unittest.main()
