import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import count_digits_letters
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(count_digits_letters.num_digits("kes123 %$ va"),(3,6,1,2))

if __name__=="__main__":
    unittest.main()
