class NoteApplication(object):

	def __init__(self, author):
		self.author = author
		self.note_list = []

	def create(self, note_content):
		self.note_content = note_content
		self.note_list.append(self.note_content)


	def list(self):
		for indx in range(len(self.note_list)):
			print "Note ID: " + str(indx) + "\n" + self.note_list[indx] + \
			"\n" "By Author " + self.author 

	def get(self, note_id):
		self.note_id = note_id
		if self.note_id in range(len(self.note_list)):
			return self.note_list[self.note_id]
		else:
			return "Note Not Found"

	def search(self, search_text):
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
		for self.note_id in self.note_list:
			if self.note_id == None:
				return "Note already deleted"
			else:
				return self.note_list.pop(self.note_id)

	def edit(self, note_id, new_content):
		self.new_content = new_content
		if self.note_id in self.note_list:
			self.note_list[self.note_id] = self.new_content
		else:
			return False





