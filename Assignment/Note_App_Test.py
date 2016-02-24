"""
​    These are the Test for the Note Application that was created.
    There are a total of 20 tests.
    The Note Application class was imported from the file
    While the unittest module was imported from python's library 
​
"""
​
import unittest
​
from Note_App import NotesApplication
​
​
class NotesApplication_Tests(unittest.TestCase):

	""" A Note Application testing class is created """
​
    def test_obj_instance1(self):
        note = NotesApplication('')
        self.assertIsInstance(note, NotesApplication, \
        	msg = "Object is not an instance of the Class")
​
    def test_obj_instance2(self):
        note = NotesApplication('author')
        self.assertIsInstance(note, NotesApplication, \
        	msg = "Object is not an instance of the Class")
​
    def test_note_list_length_1(self):
        note = NotesApplication('author', ["input1"])
        note_len = len(note.note_list)
        self.assertEqual(note_len, 1,  msg = "Note already created")
​
    def test_note_list_length_empty(self):
        note = NotesApplication('author', [])
        note_len = len(note.note_list)
        self.assertEqual(note_len, 0,  msg = "No note created")
​
    def test_create_note_empty(self): 
        note = NotesApplication("author")
        note.create("")
        note_len = len(note.note_list)
        self.assertEqual(note.create, 0,  msg = "New note not created")
​
    def test_create_note_1(self):
        note = NotesApplication('author')
        note.create('note1')
        self.assertEqual(note.create, "note1",  msg = "Success: New note created!")
​
    def test_create_note_2(self):
        note = NotesApplication("author", ["note1"])
        note.create("note2")
        note.create("note3")
        note.create("note4")
        note.create("note5")
        note_len = len(note.note_list)        
        self.assertEqual(note_len, 5,  msg = "Success: New notes created!")

    def test_create_note_3(self):
        note = NotesApplication("author", ["note1", "note2", "note3", "note4", "note5"])
        note.create("note6")
        note.create("note7")
        note.create("note8")
        note_len = len(note.note_list)        
        self.assertEqual(note_len, 8,  msg = "Success: New notes created!")

    def test_get_note_1(self):
        note = NotesApplication("author")
        test_get = note.get("")
        self.assertEqual(note.get, 0, msg = "Oops: No index passed")
​
    def test_get_note_2(self):
        note = NotesApplication("author")
        test_get = note.get(0)
        self.assertEqual(note.get, "note1", msg = "Success: Note retrieved!")

    def test_get_note_3(self):
        note = NotesApplication("author")
        test_get = note.get(3)
        self.assertEqual(note.get, "note4", msg = "Success: Note retrieved!")
​
    def test_get_note_4(self):
        note = NotesApplication("author")
        test_get = note.get(-200)
        self.assertEqual(note.get, "note4", msg = "Oops: Index out of range")

    def test_list_all_notes_1(self):
        note = NotesApplication("author", ["note1", "note2", "note3", "note4", "note5"])
        list_all = note.list()
        self.assertListEqual(note.list, ["note1", "note2", "note3", "note4", "note5"],
                             msg = "Success: All notes in the list should be listed if there are 5 notes")

    def test_list_all_notes_empty(self):
        note = NotesApplication("author", ["note1", "note2", "note3", "note4", "note5"])
        list_all = note.list()
        self.assertListEqual(note.list, [], 
        	                 msg = "Success: The list returns empty if no note created ")
​
    def test_search_1(self):
		note = NotesApplication("author", ["note1", "note2", "note3"])
		search_note = note.search("text")
		self.assertListEqual(search_note, ["note1", "note2", "note3"], 
			                 msg = "Success: search should return all notes with 'text' string")

	def test_search_empty(self):
		notes = NotesApplication("author", ["note1", "note2", "note3"])
		search_note = note.search("")
		self.assertListEqual(search_note, [], 
			                 msg = "Search should return all notes with 'text' string")

	def test_search_wrong_text(self):
		note = NotesApplication("author", ["note1", "note2", "note3"])
		search_note = notes.search("wrong_text")
		self.assertListEqual(notes_list, [], msg = "search should return an empty array"\
		                     "if the desired text is found in any notes")
​
    def test_delete_valid(self):
		note = NotesApplication("author", ["note1", "note2", "note3", "note4"])
		del_note = note.delete(2)
		note_len = len(del_note)
		self.assertEqual(note_len, 3, msg = 'Delete should reduce the size of the list')

	def test_delete_invalid_1(self):
		note = NotesApplication("author", ["note1", "note2", "note3", "note4"])
		del_note = note.delete(6)
		self.assertTrue(delete_result, True, msg = 'Delete should return True for a wrong index')

	def test_delete_invalid_2(self):
		note = NotesApplication("author", ["note1", "note2", "note3", "note4"])
		del_result = note.delete(-4)
		self.assertTrue(del_result, True, msg = 'Delete should return True for a negative index')

	def test_edit_valid_index(self):
		note = NotesApplication("author", ["note1", "note2", "note3", "note4"])
		note.edit(1, "note9")
		note_list = note.list()
		self.assertListEqual(note_list, ["note1", "note2", "note3", "note4"], msg='Edit should alter supplied index in the notes list')


	def test_edit_invalid_index(self):
		notes = NotesApplication("author", ["note1", "note2", "note3", "note4"])
		note.edit(6, "note4")
		result = notes.list()
		self.assertTrue(result, True, msg = 'Delete should return True for Invalid Index')

	def test_edit_invalid_negative(self):
		notes = NotesApplication("author", ["note1", "note2", "note3", "note4"])
		note.edit(-10, "Test Content4")
		result = note.list()
		self.assertTrue(result, True, msg = 'Return True for a negative Invalid Index')

​
if __name__ == "__main__":
	unittest.main()

		