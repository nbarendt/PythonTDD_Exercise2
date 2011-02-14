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
        self.input = input

    def getLineCount(self):
        return 0

    def getCharacterCount(self):
        return len(self.input)

    def getWordCount(self):
        return len(self.input.split())

class Test_EmptyString(unittest.TestCase):
    def setUp(self):
        self.wordCounter = WC('')

    def test_ZeroLines(self):
        self.assertEqual(0, self.wordCounter.getLineCount())

    def test_ZeroCharacters(self):
        self.assertEqual(0, self.wordCounter.getCharacterCount())
    
    def test_ZeroWords(self):
        self.assertEqual(0, self.wordCounter.getWordCount())

class Test_SingleCharacterString(unittest.TestCase):
    def setUp(self):
        self.wordCounter = WC('a')
        
    def test_0Lines(self):
        self.assertEqual(0, self.wordCounter.getLineCount())
    
    def test_1Character(self):
        self.assertEqual(1, self.wordCounter.getCharacterCount())
    
    def test_1Word(self):
        self.assertEqual(1, self.wordCounter.getWordCount())
     
