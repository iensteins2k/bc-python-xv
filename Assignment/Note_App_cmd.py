import Note_App

print "WELCOME TO NOTE APP"
author_name = raw_input("Please input Author's Name: ")
noteapp = NoteApplication(author_name)

print "READ INSTRUCTIONS BELOW"
instructions = "Enter \n '1' to create a new note "\
         "\n '2' to list a note" \
         "\n '3' to delete a note" \
         "\n '4' to search all notes" \
         "\n '5' to edit a note" \
         "\n 'q' to quit Application\n:"

user_action = ""
while user_action != "q":
    user_action = raw_input(instructions).lower()
    if user_action == '1':
        noteapp.create(notes_content)
    elif user_action == '2':
        noteapp.list()
    elif user_action == '3':
        noteapp.delete(note_id)
    elif user_action == '4':
        notesapp.search(search_text)        
    elif user_action == '5':
        edit_note = raw_input("Please enter index of note to edit: ")
        while not edit_note.isdigit():
            edit_note = raw_input("Please enter valid index of note to edit: ")
        else:
            edit_note = int(edit_note)
        edit_text = raw_input("Please enter text: ")
        noteapp.edit(edit_note, edit_text)
    elif user_action == 'q':
        break
    else:
        print("Please follow the INSTRUCTIONS carefully!")
        continue
