import sys
sys.path.append("D:\python")

import unittest
import even_odd

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(even_odd.ev_od(11),([0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9]))
    def testcase2(self):
        self.assertEqual(even_odd.ev_od(5),([0, 2, 4], [1, 3]))


if __name__=="__main__":
    unittest.main()
