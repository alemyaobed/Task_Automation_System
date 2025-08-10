from pathlib import Path
import sys
import tkinter as tk
from typing import Callable, Optional

from app.constants.constants import APP_NAME


class NoteWindow:
    """
    A single sticky note window that stays on top.
    """

    def __init__(
        self,
        title: str = APP_NAME,
        width: int = 300,
        height: int = 200,
        x: int = 100,
        y: int = 100,
        topmost: bool = True,
        bg: str = "#FFF9C4",  # light yellow
        font_family: str = "Arial",
        font_size: int = 12,
        on_close: Optional[Callable[["NoteWindow"], None]] = None,
        on_settings_change: Optional[Callable[[dict], None]] = None,
        alpha: float = 1.0,
    ) -> None:
        self.root = tk.Toplevel()
        
        icon_path = Path(__file__).parent.parent / "assets" / "snatas.ico"
        if getattr(sys, 'frozen', False):
            # Running as a bundled executable
            icon_path = Path(sys._MEIPASS) / "app" / "assets" / "snatas.ico"

        try:
            self.root.iconbitmap(default=str(icon_path))
        except Exception as e:
            print(f"Failed to load icon: {e}")
        
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.attributes("-topmost", topmost)
        self.root.configure(bg=bg)
        self.root.attributes("-alpha", alpha)

        self.text = tk.Text(
            self.root,
            wrap="word",
            font=(font_family, font_size),
            bg=bg,
            bd=0,
            undo=True,
        )
        self.text.pack(expand=True, fill="both", padx=6, pady=6)

        menu = tk.Menu(self.root)
        view_menu = tk.Menu(menu, tearoff=0)
        self._topmost_var = tk.BooleanVar(value=topmost)
        self._alpha_var = tk.DoubleVar(value=alpha)
        view_menu.add_checkbutton(
            label="Always on Top",
            onvalue=True,
            offvalue=False,
            variable=self._topmost_var,
            command=self._on_settings_update,
        )
        transparency_menu = tk.Menu(view_menu, tearoff=0)
        for i in range(10, 3, -1):
            val = i / 10.0
            transparency_menu.add_radiobutton(
                label=f"{int(val * 100)}%",
                value=val,
                variable=self._alpha_var,
                command=self._on_settings_update,
            )
        view_menu.add_cascade(label="Transparency", menu=transparency_menu)
        menu.add_cascade(label="View", menu=view_menu)
        self.root.config(menu=menu)

        self.on_close = on_close
        self.on_settings_change = on_settings_change
        self.root.protocol("WM_DELETE_WINDOW", self._handle_close)

        self._keep_on_top()

    def _keep_on_top(self) -> None:
        if self._topmost_var.get():
            self.root.lift()
        self.root.after(1, self._keep_on_top)

    def _on_settings_update(self) -> None:
        topmost = self._topmost_var.get()
        alpha = self._alpha_var.get()
        self.root.attributes("-topmost", topmost)
        self.root.attributes("-alpha", alpha)
        if self.on_settings_change:
            self.on_settings_change({"topmost": topmost, "alpha": alpha})

    def focus_text_end(self) -> None:
        self.text.focus_set()
        self.text.mark_set("insert", "end-1c")

    def get_content(self) -> str:
        return self.text.get("1.0", "end-1c")

    def set_content(self, value: str) -> None:
        self.text.delete("1.0", "end")
        self.text.insert("1.0", value)

    def _handle_close(self) -> None:
        if self.on_close:
            self.on_close(self)
        self.root.destroy()
