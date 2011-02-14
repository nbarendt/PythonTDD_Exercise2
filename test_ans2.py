import unittest

# Using TDD, create a Python class that implements the functionality of the
#  Unix "wc" command
#  Given an input string, it should compute:
#    the number of characters(bytes)
#    the number of lines
#    the number of words (white-space separated strings of characters)
#
#  For this exercise, use the test runner and put all set up code in a
#    TestCase setUp() method and only put assertions into your test_
#    methods.
#  Note, for this exercise, you can ignore Unicode versus ASCII string 
#   differences and similar differences in the size of a character
#  Note: feel free to leave both your class and your test cases
#  in the same file.

class WC(object):
    def __init__(self, input):
        pass
    def getLineCount(self):
        return 0

class Test_EmptyString(unittest.TestCase):
    def test_EmptyStringHasZeroLines(self):
        self.assertEqual(0, WC('').getLineCount())
