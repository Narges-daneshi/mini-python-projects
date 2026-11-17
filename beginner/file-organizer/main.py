from pathlib import Path
import shutil
import os


def creating_directories(base_path,file_categories):
    for category,_ in file_categories.items():
        (base_path/category).mkdir(exist_ok=True,parents=True)

def categorizing_and_moving(base_path,file_categories):
    count_move = 0
    count_replace = 0
    count_skip = 0
    items = list(base_path.iterdir())
    for item in items:
        if item.is_file():
            for category, extensions in file_categories.items():
                if item.suffix.lower() in extensions:
                    destination_file=base_path/category/item.name

                    # Check whether the destination file already exists
                    if destination_file.exists():
                        while True:
                            user_order = input("The file already exists. Do you want to replace it? (Y/N): ").strip().lower()
                            if user_order == "y":
                                os.replace(item,destination_file)
                                print("File replaced successfully!")
                                count_replace+=1
                                break

                            elif user_order == "n":
                                print("File skipped.")
                                count_skip+=1
                                break

                            else:
                                print("Please enter Y or N.")

                        break


                    else:
                        shutil.move(item, destination_file)
                        count_move+=1
                        break

    return count_move,count_replace,count_skip





file_categories = {
        "Images": {".jpg", ".jpeg", ".png", ".gif"},
        "Documents": {".pdf", ".docx", ".txt"},
        "Audio": {".mp3", ".wav"},
        "Videos": {".mp4", ".mkv"},
        "Code": {".py", ".js", ".html", ".css"},
        "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"}
    }

while True:
    base_path = Path(input("Please enter a directory path: ").strip())
    if base_path.is_dir():
        print(f"You selected '{base_path}' ")
        creating_directories(base_path, file_categories)
        count_move, count_replace, count_skip = categorizing_and_moving(base_path,file_categories)
        print("File organization completed successfully!")
        print(f"Files moved: {count_move}")
        print(f"Files replaced: {count_replace}")
        print(f"Files skipped: {count_skip}")
        break

    else:
        print("Invalid directory path. Please try again.")






