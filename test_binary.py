import unittest
from binary import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_search_empty(self):
        self.assertEqual(-1, binary_search([], 42))
    
    def test_search_failed(self):
        self.assertEqual(-1, binary_search([1,3,7,30,60,100,121], 42))
    
    def test_search_success_first_half(self):
        self.assertEqual(2, binary_search([1,4,42,57,67,100], 42))

    def test_search_success_second_half(self):
        self.assertEqual(4, binary_search([1,3,9,16,42,69], 42))
