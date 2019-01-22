# l-g-preinterview

## Description

This is a python program which takes a text file and a file containing banned words and produces a censored output to the commandline

## Files
The main program is [bannedWords.py](https://github.com/GeorgeT94/l-g-preinterview/blob/master/bannedWords/BannedWords.py)

Testing is done in [BannedWordsTest.py](https://github.com/GeorgeT94/l-g-preinterview/blob/master/Tests/BannedWordsTests.py)

The additional files are text files containing prose and lists of banned words

## How to run

Simply clone the program navigate to '/bannedWords/' and use the command
```
python bannedWords.py
```

To run the tests naviage to '/Tests/' and run 
```
python BannedWordsTests.py
```

## Documentation

The method and variable names are all as descriptive as possible meaning the code is mostly self documenting, with a couple of things explained

## Efficiency

When using a list of 1250 banned words it took 0.5seconds to censor a 500kb document
meaning it would take around 17mins per GB

In terms of memory only the banned words and one line of the file at a time are loaded, so memory usage is minimal.



