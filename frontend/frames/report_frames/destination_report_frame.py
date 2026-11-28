import customtkinter as ctk
import tkinter as tk
from frontend import THEMES as themes
from frontend.frames.report_frame import ReportFrame

THEME_BG = themes.THEME_BG
THEME_FG = themes.THEME_FG
THEME_ACCENT = themes.THEME_ACCENT
THEME_ACCENT_FG = themes.THEME_ACCENT_FG
THEME_FIELD_BG = themes.THEME_FIELD_BG
THEME_FONT_FAMILY = themes.THEME_FONT_FAMILY
THEME_FONT_SIZE = themes.THEME_FONT_SIZE

class destination_report_frame(ctk.CTkFrame):
    def __init__(self, master, db=None, **kwargs):
        super().__init__(master, fg_color=THEME_BG, **kwargs)
        self.db = db

        # Report preview
        self.report = ReportFrame(
            self
        )
        self.report.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )