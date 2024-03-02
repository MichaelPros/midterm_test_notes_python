
import json
import time

def filter_notes_by_date(notes, start_date=None, end_date=None):
    filtered_notes = []
    for note in notes:
        note_timestamp = note["timestamp"]
        if start_date and note_timestamp < start_date:
            continue
        if end_date and note_timestamp > end_date:
            continue
        filtered_notes.append(note)
    return filtered_notes

def create_note():
    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")
    note = {"title": title, "content": content, "timestamp": int(time.time())}
    notes.append(note)
    save_notes()

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

def read_notes(start_date=None, end_date=None):
    global notes
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    filtered_notes = filter_notes_by_date(notes, start_date, end_date)
    return filtered_notes

def edit_note():
    read_notes()
    note_index = int(input("Enter the index of the note you want to edit: "))
    if 0 <= note_index < len(notes):
        title = input("Enter the updated title (leave blank to keep the current title): ")
        content = input("Enter the updated content (leave blank to keep the current content): ")
        if title:
            notes[note_index]["title"] = title
        if content:
            notes[note_index]["content"] = content
        save_notes()

def delete_note():
    read_notes()
    note_index = int(input("Enter the index of the note you want to delete: "))
    if 0 <= note_index < len(notes):
        del notes[note_index]
        save_notes()

if __name__ == "__main__":
    notes = []
    while True:
        print("\n1. Create a note")
        print("2. Read notes")
        print("3. Edit a note")
        print("4. Delete a note")
        print("5. Exit")

        option = int(input("Enter the option number: "))
        if option == 1:
            create_note()
        elif option == 2:
            start_date_str = input("Enter the start date (YYYY-MM-DD): ")
            end_date_str = input("Enter the end date (YYYY-MM-DD): ")
            try:
                start_date = int(time.mktime(time.strptime(start_date_str, "%Y-%m-%d")))
                end_date = int(time.mktime(time.strptime(end_date_str, "%Y-%m-%d")))
            except ValueError:
                print("Invalid date format. Using all notes.")
                start_date = None
                end_date = None

            read_notes(start_date, end_date)
            print("Your notes:")
            for i, note in enumerate(notes):
                print(f"{i}: {note['title']} (created at {time.ctime(note['timestamp'])})")
        elif option == 3:
            edit_note()
        elif option == 4:
            delete_note()
        elif option == 5:
            break
        else:
            print("Invalid option. Please try again.")