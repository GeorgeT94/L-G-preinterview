import unittest

import time

import os, sys, io
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bannedWords.BannedWords import BannedWords

class TestBannedWords(unittest.TestCase):

    def setUp(self):
        self.bannedWords = BannedWords()
        self.capturedOutput = io.StringIO()                 
        sys.stdout = self.capturedOutput
                 
    def test_getBannedWordsList(self):
       
        self.bannedWords.setBannedWords(fileName ="BannedWords/testWords.txt")

        self.assertEqual(self.bannedWords.getBannedWordsList(), {"fudge", "secret"}, "Should be {fudge, secret}")

    def test_setBannedWordsList(self):

        self.bannedWords.setBannedWords(fileName="BannedWords/oneWord.txt")

        self.assertEqual(self.bannedWords.getBannedWordsList(),{'simple'} )

    def test_printSensoredDocument_NoBannedWords(self):
        self.bannedWords.__bannedWords = {}
        self.bannedWords.setProseFileName("Prose/basicText.txt")

        self.bannedWords.printCensoredDocument()
        sys.stdout = sys.__stdout__

        self.assertEqual(self.capturedOutput.getvalue(), "A simple sentence", "should be 'A simple sentence '")

    def test_printSensoredDocument_CensorOneWord(self):
        
        self.bannedWords.setBannedWords(fileName="BannedWords/oneWord.txt")
       
        self.bannedWords.setProseFileName(fileName="Prose/basicText.txt")

        self.bannedWords.printCensoredDocument()
        sys.stdout = sys.__stdout__

        self.assertEqual(self.capturedOutput.getvalue(), "A ****** sentence", "should be 'A ****** sentence'")

    def test_printSensoredDocument_CensorMultipleWords(self):
        self.bannedWords.setBannedWords("BannedWords/fudge-secret.txt")
        self.bannedWords.setProseFileName("Prose/fudgeProse.txt")

        self.bannedWords.printCensoredDocument()
        sys.stdout = sys.__stdout__

        self.assertEqual(self.capturedOutput.getvalue(),"There are some words that one must not say such as ***** and ****** - everything else is fine!", "should **** secret and fudge" )

    def test_printSensoredDocument_LotsOfBannedWords(self):
        self.bannedWords.setBannedWords("BannedWords/lotsOfWords.txt")
        self.bannedWords.setProseFileName("Prose/prose.txt")

        startTime = time.time()
        self.bannedWords.printCensoredDocument()
        endTime = time.time() - startTime

        self.assertLess(endTime, 0.100)

    def test_printSensoredDocument_LargeTextLotsOfBannedWords(self):
        self.bannedWords.setBannedWords("BannedWords/lotsOfWords.txt")
        self.bannedWords.setProseFileName("Prose/longProse.txt")

        startTime = time.time()
        self.bannedWords.printCensoredDocument()
        endTime = time.time() - startTime

        self.assertLess(endTime, 1)

if __name__ == '__main__':
    unittest.main()