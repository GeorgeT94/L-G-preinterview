import os, sys, io
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import re

class BannedWords():

    __proseFileName = "../Tests/Prose/prose.txt"
    __bannedWords = set()

    def setProseFileName(self , fileName):
        self.__proseFileName = fileName
    
    def setBannedWords(self, fileName):

        bannedWords = set()
        with open(fileName) as f:
            for line in f:
                if line[-1] == "\n":
                    line = line[:-1]
                bannedWords.add(line.lower())
        
        self.__bannedWords = bannedWords
        return 0
    
    def getBannedWordsList(self):
        return self.__bannedWords

    def getProseFileName(self):
        return self.__proseFileName

    
    def printCensoredDocument(self):

        with open(self.__proseFileName) as f:
            for line in f:
                splitLine = re.findall(r"[\w']+|[ .,!?;-]", line)
                for word in splitLine:
                    if word.lower() in self.__bannedWords:
                        print('*' * len(word), end='')
                    else:
                        print(word, end="")

bannedWords = BannedWords()
bannedWords.setBannedWords("../Tests/BannedWords/lotsOfWords.txt")
bannedWords.printCensoredDocument()
