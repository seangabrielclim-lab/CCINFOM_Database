import customtkinter as ctk
from frontend import THEMES as themes

THEME_BG = themes.THEME_BG
THEME_FG = themes.THEME_FG
THEME_ACCENT = themes.THEME_ACCENT
THEME_ACCENT_FG = themes.THEME_ACCENT_FG
THEME_FIELD_BG = themes.THEME_FIELD_BG
THEME_FONT_FAMILY = themes.THEME_FONT_FAMILY
THEME_FONT_SIZE = themes.THEME_FONT_SIZE

class drug_record_frame(ctk.CTkFrame):
    def __init__(self, master, db=None, **kwargs):
        super().__init__(master, fg_color="#ffffff", **kwargs)
        self.db = db

        self.record_functions = ctk.CTkTabview(self, fg_color=THEME_FIELD_BG)
        self.record_functions.add("View/Filter")
        self.record_functions.add("Add")
        self.record_functions.add("Delete")
        self.record_functions.add("Update")
        self.record_functions.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
        
        # view filter
        tab_view_filter = self.record_functions.tab("View/Filter")
        tab_view_filter.columnconfigure(0, weight=1)
        tab_view_filter.rowconfigure(0, weight=1)

        self.view_tab = filter_tab(tab_view_filter, fg_color=THEME_FIELD_BG)
        self.view_tab.grid(row=0, column=0, sticky="nsew")
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        
# view filter tab     
class filter_tab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.optionmenu4_var = ctk.StringVar()
        self.optionmenu4_var.set("Category")
        
        self.frame2 = ctk.CTkFrame(self, border_width=0, fg_color=THEME_FIELD_BG, width=350, height=60)
        self.frame2.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
        
        self.optionmenu4 = ctk.CTkOptionMenu(self.frame2, values=["Category", "Source Country", "Stock", "Period"], variable=self.optionmenu4_var, fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, width=100, height=20)
        self.optionmenu4.grid(row=1, column=0, columnspan=2, sticky="ew", padx=4, pady=4)
                
        self.frame3 = ctk.CTkFrame(self.frame2, border_width=2, fg_color=THEME_FIELD_BG, width=210, height=60)
        self.frame3.grid(row=0, column=2, rowspan=3, sticky="nsew", padx=4, pady=4)
                
        self.label1 = ctk.CTkLabel(self.frame2, text="Filter by:", text_color="#585858", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), width=90, height=26)
        self.label1.grid(row=0, column=0, sticky="", padx=4, pady=4)
        
        self.columnconfigure(0, minsize=358, weight=1)
        self.rowconfigure(0, minsize=68, weight=0)
        self.rowconfigure(1, weight=1)
                
        self.frame2.columnconfigure(0, minsize=98, weight=0)
        self.frame2.columnconfigure(1, minsize=18, weight=0)
        self.frame2.columnconfigure(2, minsize=218, weight=1)
        self.frame2.rowconfigure(0, minsize=34, weight=0)
        self.frame2.rowconfigure(1, minsize=28, weight=1)
        self.frame2.rowconfigure(2, minsize=22, weight=1)                
            