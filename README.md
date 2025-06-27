# 🗒️ SNATAS – The Sticky Notes App That Always Stays-On-Top
SNATAS is a lightweight, distraction-free sticky notes app built in Python that always stays on top of other windows. Perfect
for quick reminders, todos, or copy-paste workflows without losing focus.


## ✅ Goal: Build a Sticky Notes App That Always Stays on Top (Python-Based)
🎯 Problem
Windows Sticky Notes does not support “always-on-top,” making it inconvenient for multitasking or persistent visibility.

## ✅ Solution: Build Your Own Sticky Notes App in Python
👨‍💻 Why Build It?
Gives full control over the UX

Lets you implement always-on-top, transparency, theming, tray behavior, and more

Avoids hacking or working around the limitations of built-in Sticky Notes or extensions

## ✅ Pros & Cons of an Always-on-Top Sticky App
### 🔼 Pros
Persistent visibility (reminders, todos, quick notes)

Improves multitasking

Helpful for developers, students, creators

Customizable (transparency, themes, etc.)

### 🔽 Cons
Could be intrusive or block important windows

Might interfere with full-screen apps (video players, games)

Needs careful UI/UX (should allow minimizing/hiding)

Deviates from native Windows behavior if not well integrated

## ✅ Design Recommendations
Make “Always on Top” optional with a toggle

Allow transparency and drag-resize

Add tray icon or hotkey to hide/show notes

Autosave notes locally

## ✅ Tech Stack Options (Python)
Framework	Pros	Use Case
Tkinter	Built-in, simple, fast to prototype	✅ Best for lightweight apps
PyQt5 / PySide6	Stylish, feature-rich, good documentation	Great for scalable apps
pystray	Add system tray support	For advanced UX
pyinstaller	Create .exe	For distribution

## ✅ Sample Code: Sticky Note with Tkinter (Always on Top)
python
```
import tkinter as tk

def create_sticky_note():
    root = tk.Tk()
    root.title("Sticky Note")
    root.geometry("300x200+100+100")  # Width x Height + X + Y
    root.attributes('-topmost', True)  # Always on top
    root.configure(bg='lightyellow')

    text = tk.Text(root, wrap='word', font=('Arial', 12), bg='lightyellow', bd=0)
    text.pack(expand=True, fill='both', padx=5, pady=5)

    # Optional: Make window borderless
    # root.overrideredirect(True)

    root.mainloop()

create_sticky_note()
```
## ✅ Features You Can Add (Next Steps)
Feature	Implementation Idea
- Transparency	root.attributes('-alpha', 0.8)
- Save/Load notes	Use open() and write() with a .txt file
- Multiple notes	Use tk.Toplevel() or launch multiple windows
- Tray icon	Use pystray to hide/show from the system tray
- Hotkeys	Use keyboard or pynput to add global shortcuts



# ✅ Recommended Folder Structure for a Python Sticky Notes App
Here’s a clean and modular layout:

bash
```
sticky_notes_app/
├── main.py                 # Entry point of the app
├── notes/
│   ├── __init__.py
│   ├── note_window.py      # GUI logic for individual note windows
│   └── note_manager.py     # Handles multiple notes, saving/loading, etc.
├── storage/
│   ├── __init__.py
│   └── file_storage.py     # Save/load note content to/from disk
├── ui/
│   ├── __init__.py
│   └── theme.py            # Optional: define color themes, fonts, styles
├── assets/
│   ├── icon.ico            # Icon for the app/tray (if any)
│   └── styles.css          # (If using ttkbootstrap or themed widgets)
├── config/
│   └── settings.json       # User settings (e.g., always-on-top default)
├── requirements.txt        # For dependencies
└── README.md               # Project description
```

## 📌 Breakdown by Module
### main.py
- Initializes the app
- Loads settings
- Launches the first note or manager

### notes/note_window.py
- Handles creation of a single sticky note window
- Manages attributes like always-on-top, drag, resize, close

### notes/note_manager.py
- Manages a list of notes
- Can be used to open, close, or restore multiple notes

### storage/file_storage.py
- Save content to disk (e.g., ~/.sticky_notes/note_1.txt)
- Load previously saved notes
- Optionally autosave on close

### ui/theme.py
- Centralized styling (colors, fonts, default sizes)
- Optional support for light/dark modes

### config/settings.json
- Stores persistent app preferences (e.g., transparency, always-on-top toggle)

### assets/icon.ico
- Icon used for the tray (if you use pystray) or window

## ✅ Tools & Libraries You Might Use

| Purpose        | Library             |
|----------------|---------------------|
| GUI            | `tkinter`           |
| Tray icon      | `pystray`           |
| Hotkeys        | `keyboard`, `pynput`|
| Save/load JSON | `json` module       |
| Packaging      | `pyinstaller`       |


✅ Example Launch Flow
python
```
# main.py

from notes.note_manager import NoteManager

if __name__ == "__main__":
    manager = NoteManager()
    manager.launch()
```

## 📦 When You're Ready to Package
Once it's working, you can create a build/ or dist/ folder using:

bash
```
pyinstaller --onefile --icon=assets/icon.ico main.py
```
