# file_organizer.py

import os
import shutil
from pathlib import Path

def organize_folder(source_folder):
    if not os.path.exists(source_folder):
        print("❌ Source folder does not exist.")
        return

    # File categories
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mkv', '.mov'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Archives': ['.zip', '.rar', '.tar'],
        'Scripts': ['.py', '.js', '.html', '.css']
    }

    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            ext = Path(file).suffix.lower()
            moved = False

            for folder, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(source_folder, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    print(f"Moved: {file} → {folder}")
                    break

            if not moved:
                others_folder = os.path.join(source_folder, 'Others')
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, file))
                print(f"Moved: {file} → Others")

def main():
    print("\n🗂️ File Organizer Bot\n")
    folder = input("Enter the path of folder to organize: ").strip()
    organize_folder(folder)

if __name__ == "__main__":
    main()
