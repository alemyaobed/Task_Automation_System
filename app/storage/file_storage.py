import json
import os
from pathlib import Path
from typing import Optional


class FileStorage:
    """
    Minimal file-based storage for a single note's content and settings.
    """

    def __init__(self, app_dir: Optional[Path] = None) -> None:
        if app_dir is None:
            app_dir = Path.home() / ".snatas"
        self.app_dir = app_dir
        self.app_dir.mkdir(parents=True, exist_ok=True)
        self.last_note_file = self.app_dir / "last_note.txt"
        self.settings_file = self.app_dir / "settings.json"

    def save_last_note(self, content: str) -> None:
        self.last_note_file.write_text(content, encoding="utf-8")

    def load_last_note(self) -> str:
        if not self.last_note_file.exists():
            return ""
        return self.last_note_file.read_text(encoding="utf-8")

    def save_settings(self, settings: dict) -> None:
        self.settings_file.write_text(json.dumps(settings, indent=2), encoding="utf-8")

    def load_settings(self) -> dict:
        if not self.settings_file.exists():
            return {}
        try:
            return json.loads(self.settings_file.read_text(encoding="utf-8"))
        except Exception:
            return {}
