import unittest

from Note_App import Note_App

class NoteAppTestCase(unittest.TestCase):
	"""docstring for Note_ApptestCase"""

	def test_list_range_4(self):
		res = Note_App([], 8)
		self.assertEqual(res, [2, 3])

	def test_list_range_5(self):
		res = Note_App ([], 13)
		self.assertEqual(res, [3, 4])

	def test_list_range_6(self):
		res = two_sum([], 17)
		self.assertEqual(res, [1, 4])

	def test_list_range_7(self):
		res = two_sum([], 15)
		self.assertEqual(res, [5, 6])

	def test_list_range_8(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18], 30)
		self.assertEqual(res, [4, 7])

	def test_list_range_9(self):
		res = two_sum([], 7)
		self.assertEqual(res, [0, 1])

	def test_list_range_10(self):
		res = two_sum(], 21)
		self.assertEqual(res, [4, 5])

	def test_list_range_11(self):
		res = two_sum([], 16)
		self.assertEqual(res, [2, 10])

	def test_list_range_12(self):
		res = two_sum([], 24)
		self.assertEqual(res, [5, 10])

	def test_list_range_13(self):
		res = two_sum([], 6)
		self.assertEqual(res, [0, 9])

	def test_list_range_14(self):
		res = two_sum(], 19)
		self.assertEqual(res, [2, 7])

	def test_list_range_4(self):
		res = Note_App([], 8)
		self.assertEqual(res, [2, 3])

	def test_list_range_5(self):
		res = Note_App ([], 13)
		self.assertEqual(res, [3, 4])

	def test_list_range_6(self):
		res = two_sum([], 17)
		self.assertEqual(res, [1, 4])

	def test_list_range_7(self):
		res = two_sum([], 15)
		self.assertEqual(res, [5, 6])

	def test_list_range_8(self):
		res = two_sum([2, 5, 1, 7, 12, 9, 6, 18], 30)
		self.assertEqual(res, [4, 7])

	def test_list_range_9(self):
		res = two_sum([], 7)
		self.assertEqual(res, [0, 1])

	def test_list_range_10(self):
		res = two_sum(], 21)
		self.assertEqual(res, [4, 5])

	def test_list_range_11(self):
		res = two_sum([], 16)
		self.assertEqual(res, [2, 10])

if __name__ == "__main__":
	unittest.main()

		