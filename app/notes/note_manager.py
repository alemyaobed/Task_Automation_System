import tkinter as tk
from typing import List

from app.constants.constants import APP_NAME
from app.notes.note_window import NoteWindow
from app.storage.file_storage import FileStorage
from app.ui.theme import DEFAULT_THEME


class NoteManager:
    """
    Manages one or more NoteWindow instances and basic persistence.
    """

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the root; notes use Toplevel
        self.storage = FileStorage()
        self.notes: List[NoteWindow] = []
        self.settings = self.storage.load_settings()

    def launch(self) -> None:
        # Create the first note
        note = self.create_note()

        # Load last session content into the first note, if any
        last_content = self.storage.load_last_note()
        if last_content:
            note.set_content(last_content)
        note.focus_text_end()

        # Bind global shortcuts on root (not global OS hotkeys)
        self.root.bind_all("<Control-n>", lambda e: self.create_note())
        self.root.bind_all("<Control-s>", lambda e: self.save_active_note())
        self.root.bind_all("<Control-q>", lambda e: self.quit())

        self.root.mainloop()

    def create_note(self) -> NoteWindow:
        x_offset = 100 + len(self.notes) * 30
        y_offset = 100 + len(self.notes) * 30
        note = NoteWindow(
            title=APP_NAME,
            width=self.settings.get("width", DEFAULT_THEME["width"]),
            height=self.settings.get("height", DEFAULT_THEME["height"]),
            x=x_offset,
            y=y_offset,
            topmost=self.settings.get("topmost", DEFAULT_THEME["topmost"]),
            bg=DEFAULT_THEME["bg"],
            font_family=DEFAULT_THEME["font_family"],
            font_size=DEFAULT_THEME["font_size"],
            alpha=self.settings.get("alpha", DEFAULT_THEME.get("alpha", 1.0)),
            on_close=self._on_note_close,
            on_settings_change=self._on_settings_change,
        )
        self.notes.append(note)
        return note

    def _on_note_close(self, note: NoteWindow) -> None:
        # Save the closed note as the last note content
        self.storage.save_last_note(note.get_content())
        self.notes = [n for n in self.notes if n is not note]
        if not self.notes:
            # If all notes are closed, end the app
            self.quit()

    def _on_settings_change(self, settings: dict) -> None:
        self.settings.update(settings)
        self.storage.save_settings(self.settings)

    def save_active_note(self) -> None:
        if not self.notes:
            return
        # Save the currently last-created note's content
        self.storage.save_last_note(self.notes[-1].get_content())

    def quit(self) -> None:
        # Persist the last note (if any) before quitting
        if self.notes:
            self.storage.save_last_note(self.notes[-1].get_content())
        self.root.quit()
