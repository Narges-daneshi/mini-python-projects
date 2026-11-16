import json
from json import JSONDecodeError

# Load notes from the JSON file
def load_notes():
    try:
        with open("notes.json","r") as f:
            con=json.load(f)
            if isinstance(con, list) :
                for item in con:
                    if not isinstance(item,dict) or "title" not in item or "content" not in item :
                        print("Invalid notes file format. Starting with an empty notes list.")
                        return []
                    if not isinstance(item["title"],str) or not isinstance(item["content"],str):
                        print("Invalid notes file format. Starting with an empty notes list.")
                        return []
                return con
            else:
                print("Invalid notes file format. Starting with an empty notes list.")
                return []
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        print("Invalid notes file format. Starting with an empty notes list.")
        return []

def add_note(notes):
    print("Add a note:")
    while True:
        title=input("Title: ").strip()
        if not title:
            print("Title cannot be empty!")
            continue
        content=input("Content: ").strip()
        if not content:
            print("Content cannot be empty!")
            continue
        break
    notes.append(
        {
            "title":title,
            "content":content
        }
    )
    with open("notes.json","w") as file:
        # Save notes to the JSON file
        json.dump(notes,file,indent=4,ensure_ascii=False)
    print("Note added successfully.")

def show_notes(notes):
    if not notes:
        print("The notes list is empty. Please add a note first.")
        return
    for index,cont in enumerate(notes,start=1):
        print(f"{index}. {cont['title']}")
        print(f"   {cont['content']}")


def search_note(notes):
    search_text=(input("Enter a keyword to search: ")).lower().strip()
    if not search_text:
        print("Please enter a search term.")
        return
    situation_flag=False
    for note in notes:
        if search_text in note['title'].lower() or search_text in note['content'].lower():
            print(f"Result: {note['title']} | {note['content']}")
            situation_flag=True

    if not situation_flag:
        print("No matching notes found.")

def delete_note(notes):
    if not notes:
        print("The notes list is empty. Please add a note first.")
        return
    try:
        delete_number = int(input("Enter the number of the note to delete: "))
        if not 1<=delete_number<=len(notes):
            print("Please enter a number within the valid range.")
        else:
            deleted_note = notes.pop(delete_number - 1)
            with open("notes.json", "w") as file:
                # Save notes to the JSON file
                json.dump(notes, file,indent=4,ensure_ascii=False)
            print(f"'{deleted_note['title']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


notes=load_notes()
while True:
    print("""===== NOTES MANAGER =====
1. Add note
2. Show notes
3. Search note
4. Delete note
5. Exit """)
    print()
    option=input("Please choose a number: ").strip()
    if option=="1":
        add_note(notes)

    elif option=="2":
        show_notes(notes)

    elif option=="3":
        search_note(notes)

    elif option=="4":
        delete_note(notes)

    elif option=="5":
        print("Goodbye!")
        break
    else:
        print("Please enter a number between 1 and 5.")