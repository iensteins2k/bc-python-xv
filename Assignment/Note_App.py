"""
    This is a Class of a Note Application
    It allows users to create, view and search for notes 
"""

class NoteApplication(object):


	def __init__(self, author):

		"""
			This creates a 'constructor' that initialises the Note applications
			This also initialises an empty list called note_lists that 
			stores tha parameters of the notes created 		
		"""
		self.author = author
		self.note_list = []

	def create(self, note_content):
		"""
			This method allows users create notes and
			It then stores to  note_list. 		
		"""
		self.note_content = note_content
		self.note_list.append(self.note_content)


	def list(self):
		"""
			This method allows loops through the entire list of notes,
			and prints all the notes created.  		
		"""
		for indx in range(len(self.note_list)):
			print "Note ID: " + str(indx) + "\n" + self.note_list[indx] + \
				  1"\n" "By Author " + self.author self

	def get(self, note_id):
		"""
			This method the id number of a note in the list,
			and returns the notes associated with the id number.  		
		"""
		self.note_id = note_id
		if self.note_id in range(len(self.note_list)):
			return self.note_list[self.note_id]
		else:
			return "Note Not Found"

	def search(self, search_text):
		"""
           This method searches for a text in the list ,
           and returns the all notes in which the text appears.  		
		"""
		self.search_text = search_text	
		print "Showing results for search %s" % self.search_text + "\n"                                                   	
		       search_app = filter(lambda x: self.search_text in x, self.note_list)
		if len(search_app) == 0:
			print "No results for  %s" % self.search_text

		else:
			for id, note in enumerate(search_app):
				print "Note ID: " + str(id) + "\n" + self.note_list + \
					  "By Author: " + self.author

	def delete(self, note_id):
		"""
			This method deletes a created note based on a the id number
			of the note and returns a message if the note has already been deleted.  		
		"""
		for self.note_id in self.note_list:
			if self.note_id == None:
				return "Note already deleted"
			else:
				return self.note_list.pop(self.note_id)

	def edit(self, note_id, new_content):
		"""
			This method edits a created note and returns the it to the list.  		
		"""
		self.new_content = new_content
		if self.note_id in self.note_list:
			self.note_list[self.note_id] = self.new_content
		else:
			return False

"""
	This is an instance of a the Note Application Class named Baju
"""
author = NoteApplication("Baju")



