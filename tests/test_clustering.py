# test_clustering.py
import unittest
from quantum_algorithms.clustering import quantum_clustering
import numpy as np

class TestClustering(unittest.TestCase):

    def test_clustering(self):
        data = np.random.rand(10, 2)  # Generate random data for testing
        result = quantum_clustering(data)
        self.assertIsNone(result)  # No result is expected from this function, just visualization

if __name__ == '__main__':
    unittest.main()
