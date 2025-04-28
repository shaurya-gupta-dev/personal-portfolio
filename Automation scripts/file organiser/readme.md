# File Organizer

A Python-based file organization script designed to automatically categorize files into their respective folders. The script identifies file types based on their extensions and moves them into predefined categories such as Images, Videos, Documents, Archives, and Scripts. Any files that do not fit into these categories are moved to an "Others" folder.

## Features

- Automatically organizes files into subfolders based on their extensions.
- Supports categorization for:
  - Images (`.jpg`, `.jpeg`, `.png`, `.gif`)
  - Videos (`.mp4`, `.mkv`, `.mov`)
  - Documents (`.pdf`, `.docx`, `.txt`, `.pptx`)
  - Archives (`.zip`, `.rar`, `.tar`)
  - Scripts (`.py`, `.js`, `.html`, `.css`)
  - Others (for files that don't match any category)
- Easy to use with a simple command-line interface (CLI).

## Requirements

- Python 3.x
- `os` and `shutil` libraries (both are built-in Python libraries, no installation required)

## Usage
1- Run the script using the command line:
  ```bash
  python file_organizer.py
```

2- Enter the path of the folder you want to organize when prompted.
- ex- 
3- The script will categorize the files into appropriate subfolders within the specified folder.

## How It Works
- The script first checks if the specified folder exists.

- It then iterates over each file in the folder, checking the file extension.

- Based on the file extension, it moves the file to the appropriate subfolder:

- If the file type matches one of the predefined categories, it’s moved accordingly.

- If the file type doesn’t match any of the predefined categories, it’s moved to an "Others" folder.

- Each file’s movement is logged to the terminal with a message indicating where it has been moved.

##Customization
- You can easily modify the file_types dictionary to add more categories or file extensions according to your needs. For example, you can add .mp3 for audio files, .xlsx for Excel files, etc.

  ## Example

```bash
  🗂️ File Organizer Bot

Enter the path of folder to organize: /path/to/your/folder
Moved: photo.jpg → Images
Moved: video.mp4 → Videos
Moved: document.pdf → Documents
Moved: archive.zip → Archives
Moved: script.py → Scripts
Moved: file.xyz → Others
```
