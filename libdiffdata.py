#!/usr/bin/env python

import unittest

def indexOfMin(values):
    return values.index(min(values))

def indexOfMinDiffs(diffs):
    return indexOfMin([abs(a-b) for a,b in diffs])
    
def indexOfLowestVariation(lowGoals, highGoals):    
    """ Returns index of variation between list of goals for, goals against """
    tuples = zip(highGoals, lowGoals)
    return indexOfMinDiffs(tuples)

def indexOfLowestVariance(dataset):
    return indexOfMinDiffs(dataset)+1
    
def parseLine():
    pass
    
#
# Tests
#
class LibDiffDataTestSuite(unittest.TestCase):
    def testVariation(self):
        self.assertEqual(indexOfLowestVariation([1,1,1],[3,2,3]), 1, "lowest variation found in dataset")
        
    def testIndexOfMin(self):
        self.assertEqual(indexOfMin([2,3,4,1,2,3,4]), 3, "Index of minimum value")
        
    def testDataSet(self):
        testData = [(93, 29), (89, 33)]
        self.assertEqual(indexOfLowestVariance(testData), 2, "Index of Lowest score failed")
        
    def testParseAndExtract(self)
        self.assertEqual(parseLine("a b 23 2 ob", 2,4, (23,"ob")), (), "")
        
if __name__ == '__main__':
    unittest.main()
