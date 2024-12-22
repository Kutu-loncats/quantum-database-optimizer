# test_grover.py
import unittest
from quantum_algorithms.grover_search import grover_search

class TestGroverSearch(unittest.TestCase):

    def test_grover_search(self):
        result = grover_search()
        self.assertIn('5', result)  # Ensure we find the target at index 5

if __name__ == '__main__':
    unittest.main()
