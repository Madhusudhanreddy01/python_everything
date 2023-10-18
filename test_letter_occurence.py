import sys
sys.path.append("D:\Python\program+u\programs")

import unittest
import letter_occurence

class Testletter(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(letter_occurence.letter_("ABCDCDC", "CDC"), ("The number of occurrences of", "CDC", "in", "ABCDCDC", "is", 2))
    def testcase2(self):
        self.assertEqual(letter_occurence.letter_("ABCABCABC", "ABC"), ("The number of occurrences of", "ABC", "in", "ABCABCABC", "is", 3))



if __name__=="__main__":
    unittest.main()