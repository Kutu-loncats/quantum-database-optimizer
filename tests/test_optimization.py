# test_optimization.py
import unittest
from quantum_algorithms.optimization import optimize_query

class TestOptimization(unittest.TestCase):

    def test_optimization(self):
        result = optimize_query()
        self.assertLess(result, 1.0)  # Optimization should return a value less than 1

if __name__ == '__main__':
    unittest.main()
