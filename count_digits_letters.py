#Python Program to Count the Number of Digits and Letters in a String
#import unittest
#class Testadd(unittest.TestCase):
#    def testcase(self):
#        self.assertEqual(num_digits(input("enter ur string: ")),(5,4,3,2))
def num_digits(s):
    d = 0
    l = 0
    y=0
    sp = 0
    special="(!@3$5^~&*?><\/.,)"
    for i in s:
        if i.isdigit():
            d += 1
        elif i in special:
            y += 1
        elif i == " ":
            sp += 1
        else:
            l += 1
            
    return (d,l,y,sp)

print(num_digits("kesav123$ &"))

#if __name__=="__main__":
#    unittest.main()
