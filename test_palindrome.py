import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import palindrome

class Testpalindrome_(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(palindrome.pal("MADAM"), "Palindrome")
    def testcase2(self):
        self.assertEqual(palindrome.pal("madhu"), "Not a Palindrome")


if __name__=="__main__":
    unittest.main()