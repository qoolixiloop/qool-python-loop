#!/usr/bin/python
import unittest
from levdist import LevDist

class TestLevDist(unittest.TestCase):
	def setUp(self):
		self.levDist = LevDist()
	
	def test_left_empty(self):
		actual = self.levDist.compute("", "this")
		expected = 4
		self.assertEqual(expected, actual)
	
	def test_apples_oranges(self):
		actual = self.levDist.compute("apples", "oranges")
		expected = 5
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()
