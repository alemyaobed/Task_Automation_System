"""
SNATAS MVP entry point.

Launches a minimal always-on-top sticky notes app using Tkinter.
"""
from app.notes.note_manager import NoteManager


def main() -> None:
    manager = NoteManager()
    manager.launch()


if __name__ == "__main__":
    main()
