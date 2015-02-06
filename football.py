#!/usr/bin/env python

import unittest
import libdiffdata as ld


    

def grabGoalsFA(line):
    tokens = line.split()
    return (int(tokens[6]), int(tokens[8]))
    
def collateFAFromFile(filename):
    lines = open(filename).readlines()
    del lines[0]
    return [grabGoalsFA(line) for line in lines if "--" not in line]

def lowestGoalDiff(filename):
    return ld.indexOfLowestVariance(collateFAFromFile(filename))
    
#
# Tests
#
class FootballKataTestSuite(unittest.TestCase):
        
    def testLineParsing(self):
        self.assertEqual(grabGoalsFA("    2. Manchester_U    38    28   5   5    89  -  33    89"), (89, 33), "Parse goal scores")   
        
    def testReadAndParseFile(self):
        foo = collateFAFromFile("football.txt")
        self.assertEqual(foo[0], (93, 29), "Tuple mismatch for expected first goal FA")
        self.assertEqual(foo[-1], (40, 82), "Tuple mismatch for expected last goal FA")
        
    def testIndexOfLowestDiff(self):
        self.assertEqual(lowestGoalDiff("football.txt"), 13, "Find the right diff from test data set") 

if __name__ == '__main__':
    unittest.main()


