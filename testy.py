#!/usr/bin/env python

import unittest
    
#
# Tests
#
class LibDiffDataTestSuite(unittest.TestCase):
    def testVariation(self):
        self.assertEqual(7, 7)
        
if __name__ == '__main__':
    unittest.main()
