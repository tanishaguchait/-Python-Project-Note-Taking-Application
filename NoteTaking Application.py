import os

# Note-Taking Application

def display_menu():
    print("\n--- Note-Taking Application Menu ---")
    print("1. Add a note")
    print("2. View notes")
    print("3. Delete a note")
    print("4. Save notes to file")
    print("5. Load notes from file")
    print("6. Exit")
    print("------------------------------------")

def add_note(notes):
    note = input("Enter a note: ")
    notes.append(note)
    print("Note added successfully.")

def view_notes(notes):
    if not notes:
        print("No notes available.")
    else:
        print("\n--- Your Notes ---")
        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note}")
        print("------------------")

def delete_note(notes):
    view_notes(notes)
    if notes:
        try:
            note_num = int(input("Enter the note number to delete: "))
            if 1 <= note_num <= len(notes):
                removed_note = notes.pop(note_num - 1)
                print(f"Note '{removed_note}' deleted successfully.")
            else:
                print("Invalid note number.")
        except ValueError:
            print("Please enter a valid number.")

def save_notes_to_file(notes, filename):
    with open(filename, 'w') as file:
        for note in notes:
            file.write(note + "\n")
    print(f"Notes saved to {filename}.")

def load_notes_from_file(notes, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            notes.clear()
            for line in file:
                notes.append(line.strip())
        print(f"Notes loaded from {filename}.")
    else:
        print(f"No file named {filename} found.")

def main():
    notes = []
    filename = "notes.txt"
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            save_notes_to_file(notes, filename)
        elif choice == '5':
            load_notes_from_file(notes, filename)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

