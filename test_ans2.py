import unittest

class WC(object):
    def __init__(self, input):
        self.input = input

    def getLineCount(self):
        return self.input.count('\n')

    def getCharacterCount(self):
        return len(self.input)

    def getWordCount(self):
        return len(self.input.split())

class Test_EmptyInput(unittest.TestCase):
    def setUp(self):
        self.wordCounter = WC('')

    def test_ZeroLines(self):
        self.assertEqual(0, self.wordCounter.getLineCount())

    def test_ZeroCharacters(self):
        self.assertEqual(0, self.wordCounter.getCharacterCount())
    
    def test_ZeroWords(self):
        self.assertEqual(0, self.wordCounter.getWordCount())

class Test_SingleCharacterInput(unittest.TestCase):
    def setUp(self):
        self.wordCounter = WC('a')
        
    def test_ZeroLines(self):
        self.assertEqual(0, self.wordCounter.getLineCount())
    
    def test_One1Character(self):
        self.assertEqual(1, self.wordCounter.getCharacterCount())
    
    def test_OneWord(self):
        self.assertEqual(1, self.wordCounter.getWordCount())
     
class Test_TwoWordInput(unittest.TestCase):
    def setUp(self):
        self.wordCounter = WC('a b')
        
    def test_ZeroLines(self):
        self.assertEqual(0, self.wordCounter.getLineCount())

    def test_ThreeCharacters(self):
        self.assertEqual(3, self.wordCounter.getCharacterCount())
    
    def test_TwoWords(self):
        self.assertEqual(2, self.wordCounter.getWordCount())

class Test_InputWithNewLine(unittest.TestCase):
    def setUp(self):
        self.wordCounter = WC('a\n')

    def test_OneLine(self):
        self.assertEqual(1, self.wordCounter.getLineCount())

    def test_TwoCharacters(self):
        self.assertEqual(2, self.wordCounter.getCharacterCount())
    
    def test_OneWord(self):
        self.assertEqual(1, self.wordCounter.getWordCount())

class Test_MultiLineInput(unittest.TestCase):
    def setUp(self):
        self.wordCounter = WC('hello world!\ngoodbye world!\n')

    def test_TwoLines(self):
        self.assertEqual(2, self.wordCounter.getLineCount())
    
    def test_TwentyEightCharacters(self):
        self.assertEqual(28, self.wordCounter.getCharacterCount())
    
    def test_FourWords(self):
        self.assertEqual(4, self.wordCounter.getWordCount())

