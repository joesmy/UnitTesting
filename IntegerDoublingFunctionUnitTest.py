# Integer Doubling Function Unit Test

import unittest


def twiceNumber(a):
    return a*2 

class TestNum(unittest.TestCase):

    def testDouble(self):
        result = twiceNumber(17)
        self.assertEqual(result,34)

if __name__ == '__main__':
    unittest.main()
        





