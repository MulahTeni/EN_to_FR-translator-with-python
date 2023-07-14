"""
    Unit Testing for Translation Functions
"""
import unittest
from translator import english_to_french, french_to_english

class test_englishToFrench(unittest.TestCase):
    # Class for testing e2f
    def test1(self):
        #   test for hello
        #   when testing hello translated to Pepitoooo?
        self.assertEqual(english_to_french('Hey'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hey'), 'hello')

class test_frenchToEnglish(unittest.TestCase):
    # Class for testing f2e
    def test1(self):
        #test for hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()
