# module to test mean, correlation and standard deviation functions to ensure robustness.
import unittest
import sys
import os
sys.path.append(os.path.abspath(r"C:\Users\Varun\OneDrive\Documents\stock-analysis-ml-roadmap\learning"))


from learning import mean
class TestCalculations(unittest.TestCase):
    def setUp(self):
        pass
    def test_mean(self, arr):
        self.assertEqual(arr) == 50.27272 # arr = [0,7,5,4,3,2,99,44,224,67,98]



