# 📂 Smart Files Organizer

A **Python-based file management tool** that helps organize messy folders, find duplicate files, and undo the last file-moving operation.

This project was built to practice Python file handling, path management, hashing, logging, and automation using the standard Python library.

---

## ✨ Features

### 📁 1. Organize Files by Type

Automatically sorts files into folders according to their extensions.

For example:

```text
📂 Selected Folder
│
├── 📂 Images
│   ├── photo.jpg
│   └── wallpaper.png
│
├── 📂 Documents
│   ├── notes.pdf
│   └── resume.docx
│
├── 📂 Python
│   └── program.py
│
├── 📂 Videos
│   └── movie.mp4
│
└── 📂 Others
    └── unknown.xyz
```

The file categories and their extensions are maintained separately in `file_categories.py`.

Currently supported categories include:

* 🖼️ Images
* 📄 Documents
* 📊 Spreadsheets
* 📽️ Presentations
* 🎵 Music
* 🎬 Videos
* 📦 Archives
* 🐍 Python
* 💻 Programming
* 🗄️ Databases
* 🔤 Fonts
* ⚙️ Executables
* 🛠️ Configuration
* 📝 Logs
* 💬 Subtitles

---

### 🕒 2. Organize Files by Time

Files can also be organized according to when they were modified.

Available options:

* **Today / Yesterday / Others**
* **Specific Date**
* **Month**
* **Year**

Example:

```text
📂 Selected Folder
│
├── 📂 Today
├── 📂 Yesterday
└── 📂 Others
```

Date-based organization can also create folders such as:

```text
📂 15-9-2026
📂 14-9-2026
```

or:

```text
📂 9-2026
📂 8-2026
```

---

## 🔎 3. Find Duplicate Files

The project includes a duplicate-file detection system.

Instead of comparing every file directly, it uses a two-step process:

### Step 1 — Compare File Size

Files with different sizes cannot be identical.

So files are first grouped according to their size.

### Step 2 — Compare SHA-256 Hash

Files having the same size are then hashed using:

```python
hashlib.sha256()
```

Files with the same SHA-256 hash are considered duplicates.

This reduces unnecessary hash calculations and makes the duplicate search more efficient.

---

## 🗑️ 4. Merge Duplicate Files

After duplicate files are found, the program allows the user to merge a duplicate group.

The user can:

1. Provide a new name.
2. Keep one copy.
3. Permanently delete the remaining duplicate copies.

⚠️ **Important:** This operation permanently deletes duplicate files, so make sure you have a backup of important data before using it.

---

## ↩️ 5. Undo Last Operation

The organizer maintains an activity log using Python's `logging` module.

Each moving operation receives a unique ID generated using:

```python
uuid.uuid4()
```

The log stores information about:

* Original file location
* New file location
* Operation ID
* Start and end of the operation

The program can use this information to reverse the **last file-moving operation**.

Example:

```text
Original Location
        ↓
   Move File
        ↓
New Location
        ↓
     Undo
        ↓
Original Location
```

---

## 📜 6. Activity Log

The project records file operations in:

```text
trial.log
```

The log can be viewed from the main menu to inspect the most recent operation.

Example log information:

```text
Moving Process Started
File Moved
Moved to
Moving Process Ended
```

This makes it easier to track what the program has done.

---

# 🛠️ Technologies Used

This project is built entirely with Python's standard library.

| Module    | Purpose                            |
| --------- | ---------------------------------- |
| `pathlib` | Working with files and directories |
| `shutil`  | Moving files                       |
| `os`      | Directory operations               |
| `time`    | File date/time information         |
| `hashlib` | SHA-256 file hashing               |
| `logging` | Recording file operations          |
| `uuid`    | Generating unique operation IDs    |

No external Python packages are required.

---

# 📂 Project Structure

```text
Smart-files-organizer/
│
├── main.py
├── file_categories.py
└── README.md
```

### `main.py`

Contains the main functionality of the application, including:

* Path validation
* File and folder detection
* File organization
* Date/time sorting
* Duplicate detection
* Duplicate merging
* Undo functionality
* Activity-log viewing
* User interface/menu

### `file_categories.py`

Contains the extension-to-category mapping used when organizing files.

Example:

```python
"Images": [".jpg", ".jpeg", ".png", ".gif"]
```

---

# 🚀 Getting Started

## Prerequisites

You need **Python 3** installed on your computer.

Check your Python installation:

```bash
python --version
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/ganshuman596-dev/Smart-files-organizer.git
```

Move into the project directory:

```bash
cd Smart-files-organizer
```

---

## ▶️ Run the Program

Run:

```bash
python main.py
```

You should see the main menu:

```text
==================================================
           Welcome to SMART FILE MANAGER
==================================================

1. Organize files
2. Find duplicates
3. Undo last operation
4. View last action activity log
5. Exit
```

---

# 🧭 How to Use

### Organize Files

Choose:

```text
1. Organize files
```

Then select your preferred organization method:

```text
1. Sort by file type
2. Sort by Today/Yesterday/Others
3. Sort by date
4. Sort by month
5. Sort by year
```

Enter the folder path you want to organize.

Example:

```text
F:\Downloads
```

---

### Find Duplicate Files

Choose:

```text
2. Find duplicates
```

Enter the folder path.

The program will identify groups of duplicate files using file size and SHA-256 hashing.

You can then choose whether to skip or merge a duplicate group.

---

### Undo Last Operation

Choose:

```text
3. Undo last operation
```

The program reads the activity log and attempts to reverse the most recent moving operation.

---

### View Activity Log

Choose:

```text
4. View last action activity log
```

This displays information about the most recent operation recorded in the log.

---

# 🧠 What I Learned From This Project

This project helped me understand several important Python concepts:

* Working with files and folders
* `pathlib`
* File paths and extensions
* `shutil.move()`
* File metadata using `stat()`
* File modification time
* `hashlib` and SHA-256
* Dictionaries and grouping
* Reading and processing log files
* Regular file-position operations such as `seek()` and `tell()`
* `logging`
* Generating unique IDs using `uuid`
* Building menu-driven Python programs
* Breaking a large program into functions
* Working with multiple Python modules

---

# ⚠️ Important Safety Note

This program performs real file operations.

The duplicate merging feature can **permanently delete duplicate files**.

Therefore:

> **Always keep a backup of important files before testing the organizer on important folders.**

For learning and testing, it is recommended to create a temporary folder containing sample files first.

---

# 🔮 Future Improvements

Some features that could make the project more robust in future versions:

* [ ] Graphical User Interface
* [ ] Better error handling
* [ ] File name collision handling
* [ ] Recursive folder organization
* [ ] Preview changes before moving files
* [ ] Multiple undo levels
* [ ] More advanced logging
* [ ] Configuration file for custom categories
* [ ] Search and filter functionality
* [ ] File size-based organization
* [ ] More detailed duplicate reports
* [ ] Improved cross-platform support

---

# 🤝 Contributing

This project is primarily a learning project, but suggestions and improvements are welcome.

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

# ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 👨‍💻 Author

**Anshuman Gaikwad**

Built with ❤️ and Python 🐍

### Repository

[Smart Files Organizer on GitHub](https://github.com/ganshuman596-dev/Smart-files-organizer?utm_source=chatgpt.com)

