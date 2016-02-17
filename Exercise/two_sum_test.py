import unittest

from two_sum import two_sum

class TwoSumTestCase(unittest.TestCase):
	"""docstring for TwoSumTestCase"""

	def test_list_range_4(self):
		res = two_sum([2, 5, 1, 7], 8)
		self.assertEqual(res, [2, 3])

	def test_list_range_5(self):
		res = two_sum([2, 5, 1, 7, 6], 13)
		self.assertEqual(res, [3, 4])

	def test_list_range_6(self):
		res = two_sum([2, 5, 1, 7, 12, 9], 17)
		self.assertEqual(res, [1, 4])

	def test_list_range_7(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6], 15)
		self.assertEqual(res, [5, 6])

	def test_list_range_8(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18], 30)
		self.assertEqual(res, [4, 7])

	def test_list_range_9(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18, 3], 7)
		self.assertEqual(res, [0, 1])

	def test_list_range_10(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18, 3, 4], 21)
		self.assertEqual(res, [4, 5])

	def test_list_range_11(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18, 3, 4, 15], 16)
		self.assertEqual(res, [2, 10])

	def test_list_range_12(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18, 3, 4, 15, 10], 24)
		self.assertEqual(res, [5, 10])

	def test_list_range_13(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18, 3, 4, 15, 10, 19], 6)
		self.assertEqual(res, [0, 9])

	def test_list_range_14(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18, 3, 4, 15, 10, 19, 20], 19)
		self.assertEqual(res, [2, 7])

if __name__ == "__main__":
	unittest.main()

		