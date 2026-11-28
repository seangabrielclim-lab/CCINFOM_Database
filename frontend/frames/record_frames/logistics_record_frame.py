import customtkinter as ctk
import tkinter as tk
from frontend import THEMES as themes
from tkcalendar import DateEntry
from frontend.frames.record_table import RecordTable
from frontend.frames.record_form import RecordForm, DeleteRecord

THEME_BG = themes.THEME_BG
THEME_FG = themes.THEME_FG
THEME_ACCENT = themes.THEME_ACCENT
THEME_ACCENT_FG = themes.THEME_ACCENT_FG
THEME_FIELD_BG = themes.THEME_FIELD_BG
THEME_FONT_FAMILY = themes.THEME_FONT_FAMILY
THEME_FONT_SIZE = themes.THEME_FONT_SIZE

# main frame
class logistics_record_frame(ctk.CTkFrame):
    def __init__(self, master, db=None, **kwargs):
        super().__init__(master, fg_color=THEME_BG, **kwargs)
        self.db = db
        
        # view filter tab
        tab_view_filter = master.tab("View/Filter")
        tab_view_filter.columnconfigure(0, weight=1)
        tab_view_filter.rowconfigure(0, weight=1)
        filter_tab(tab_view_filter, fg_color=THEME_BG).grid(row=0, column=0, sticky="nsew")
        
        # add tab
        tab_add = master.tab("Add")
        tab_add.columnconfigure(0, weight=1)
        tab_add.rowconfigure(0, weight=1)
        add_tab(tab_add, fg_color=THEME_BG).grid(row=0, column=0, sticky="nsew")
        
        # update tab
        tab_update = master.tab("Update")
        tab_update.columnconfigure(0, weight=1)
        tab_update.rowconfigure(0, weight=1)
        update_tab(tab_update, fg_color=THEME_BG).grid(row=0, column=0, sticky="nsew")
        
        # delete tab
        tab_delete = master.tab("Delete")
        tab_delete.columnconfigure(0, weight=1)
        tab_delete.rowconfigure(0, weight=1)
        delete_tab(tab_delete, fg_color=THEME_BG).grid(row=0, column=0, sticky="nsew")
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        
# view filter tab     
class filter_tab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.options_var = ctk.StringVar()
        self.options_var.set("Category")
        
        self.fields = ctk.CTkFrame(self, border_width=0, fg_color=THEME_BG, width=350, height=60)
        self.fields.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
        
        self.options = ctk.CTkOptionMenu(
            self.fields, 
            values=["Category", "Source Country", "Stock", "Period"], 
            variable=self.options_var, command=self.on_change,
            fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, width=100, height=30
        )
        
        self.options.grid(row=1, column=0, columnspan=2, sticky="ew", padx=4, pady=4)
                
        self.input_frame = ctk.CTkFrame(self.fields, fg_color=THEME_FG, width=210, height=60)
        self.input_frame.grid(row=0, column=2, rowspan=3, sticky="nsew", padx=4, pady=4)
                
        ctk.CTkLabel(
            self.fields, text="Filter by:", 
            text_color="#FFFFFF", 
            font=ctk.CTkFont(family="Helvetica", size=THEME_FONT_SIZE, weight="bold"), 
            width=90, height=26
        ).grid(row=0, column=0, sticky="", padx=4, pady=4)
        
        # creates subframes. Will be shown depending on choice
        self.filter_frames = {
            "Category" : self.category_frame(),
            "Source Country": self.country_frame(),
            "Stock" : self.stock_frame(),
            "Period" : self.period_frame(),
        }
        
        # Shows the default subframe
        for frame in self.filter_frames.values():
            frame.grid(row=0, column=0, sticky="nsew", padx=6, pady=6)
            frame.grid_remove()
        self.on_change(self.options_var.get())
        
        # table
        self.table = RecordTable(self)
        self.table.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)
        
        self.columnconfigure(0, minsize=358, weight=1)
        self.rowconfigure(0, minsize=68, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
                
        self.fields.columnconfigure(0, minsize=98, weight=0)
        self.fields.columnconfigure(1, weight=0)
        self.fields.columnconfigure(2, weight=1)
        self.fields.rowconfigure(0, minsize=34, weight=0)
        self.fields.rowconfigure(1, weight=1)
      
    # Changes subframe when option is changed  
    def on_change(self, selected_frame):
        for frame in self.filter_frames.values():
            frame.grid_remove()
        self.filter_frames[selected_frame].grid() 
     
    # creates a category frame   
    def category_frame(self):
        frame = ctk.CTkFrame(self.input_frame, fg_color="transparent")
        
        self.category_option_var = ctk.StringVar()
        self.category_option_var.set("Category 1")
        
        ctk.CTkLabel(
            frame, text="Category:", 
            font = ctk.CTkFont(family="Helvetica", size=THEME_FONT_SIZE, weight="bold"),
            text_color="#FFFFFF"
        ).grid(row=1, column=1, padx=6, pady=6, sticky="w")
        
        self.category_option = ctk.CTkOptionMenu(
            frame, 
            values=["Category 1", "Category 2"], variable=self.category_option_var, 
            fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, height=28
        )
        self.category_option.grid(row=1, column=2, sticky="ew", padx=4, pady=4)

        self.execute_command = ctk.CTkButton(
            frame, text="Execute", 
            command=self.on_execute_category_command, 
            fg_color="#79a267", 
            font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), 
            text_color=THEME_ACCENT_FG, width=80, height=30
        )
        self.execute_command.grid(row=1, column=3, sticky="ew", padx=4, pady=4)
        
        frame.rowconfigure(0, minsize=18, weight=1)
        frame.rowconfigure(1, weight=0)
        frame.columnconfigure(0, minsize=80, weight=1) 
        frame.columnconfigure(1, weight=0) 
        frame.columnconfigure(2, weight=0) 
        frame.columnconfigure(3, weight=0)
        frame.columnconfigure(4, weight=1)
        return frame
    
    # executes category command
    def on_execute_category_command(self):
        pass 
    
    # creates the country fields frame
    def country_frame(self):
        frame = ctk.CTkFrame(self.input_frame, fg_color="transparent")        
        
        ctk.CTkLabel(
            frame, text="Country:", 
            text_color="#FFFFFF", 
            font=ctk.CTkFont(family="Helvetica", size=THEME_FONT_SIZE, weight="bold"), 
            width=90, height=26
        ).grid(row=1, column=1, sticky="", padx=4, pady=4)
        
        self.country_entry = ctk.CTkEntry(frame, placeholder_text="Enter source country...", fg_color=THEME_FG, text_color=THEME_FIELD_BG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=12), width=200, height=30)
        self.country_entry.grid(row=1, column=2, sticky="w", padx=4, pady=4)
        
        self.execute_command = ctk.CTkButton(
            frame, text="Execute", 
            command=self.on_execute_country_command, 
            fg_color="#79a267", 
            font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), 
            text_color=THEME_ACCENT_FG, width=80, height=30
        )
        self.execute_command.grid(row=1, column=3, sticky="ew", padx=4, pady=4)
        
        frame.rowconfigure(0, minsize=18, weight=1)
        frame.rowconfigure(1, weight=0)
        frame.columnconfigure(0, minsize=80, weight=1) 
        frame.columnconfigure(1, weight=0) 
        frame.columnconfigure(2, weight=0) 
        frame.columnconfigure(3, weight=0)
        frame.columnconfigure(4, weight=1)
        return frame
    
    # executes country command
    def on_execute_country_command(self):
        pass 

    # creates the stock fields frame
    def stock_frame(self):
        frame = ctk.CTkFrame(self.input_frame, fg_color="transparent")

        ctk.CTkLabel(
            frame, text="Stock Quantity(default: less than minimum stock level):", 
            text_color="#FFFFFF", 
            font=ctk.CTkFont(family="Helvetica", size=THEME_FONT_SIZE, weight="bold"), 
            width=90, height=26
        ).grid(row=1, column=1, sticky="", padx=4, pady=4)
        
        self.stock_entry= tk.Spinbox(
            frame, 
            from_=0, to=999999, 
            bg = THEME_ACCENT_FG,
            font=ctk.CTkFont(family="Helvetica", size=THEME_FONT_SIZE, weight="bold")
        )
        self.stock_entry.grid(row=1, column=2, sticky="ew", padx=4, pady=4)
        
        self.execute_command = ctk.CTkButton(
            frame, text="Execute", 
            command=self.on_execute_stock_command, 
            fg_color="#79a267", 
            font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), 
            text_color=THEME_ACCENT_FG, width=80, height=30
        )
        self.execute_command.grid(row=1, column=3, sticky="ew", padx=4, pady=4)
        
        frame.rowconfigure(0, minsize=18, weight=1)
        frame.rowconfigure(1, weight=0)
        frame.columnconfigure(0, minsize=80, weight=1) 
        frame.columnconfigure(1, weight=0) 
        frame.columnconfigure(2, weight=0) 
        frame.columnconfigure(3, weight=0)
        frame.columnconfigure(4, weight=1)
        
        return frame
    
    # executes stock command
    def on_execute_stock_command(self):
        pass 

    # creates the period fields frame
    def period_frame(self):
        frame = ctk.CTkFrame(self.input_frame, fg_color="transparent")

        ctk.CTkLabel(
            frame, text="Select a time period:", 
            text_color="#FFFFFF", 
            font=ctk.CTkFont(family="Helvetica", size=THEME_FONT_SIZE, weight="bold"), 
            width=90, height=26
        ).grid(row=1, column=1, sticky="", padx=4, pady=4)
        
        self.date_entry = DateEntry(frame, date_pattern="yyyy-mm-dd")
        self.date_entry.grid(row=1, column=2, sticky="w", padx=4, pady=4)
        
        self.execute_command = ctk.CTkButton(
            frame, text="Execute", 
            command=self.on_execute_period_command, 
            fg_color="#79a267", 
            font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), 
            text_color=THEME_ACCENT_FG, width=80, height=30
        )
        self.execute_command.grid(row=1, column=3, sticky="ew", padx=4, pady=4)
        # ensures that the date selection pop up closes when switching tabs
        self.date_entry.bind("<Unmap>", lambda _e: self.date_entry.drop_down() if self.date_entry._top_cal.winfo_ismapped() else None)
        
        frame.rowconfigure(0, minsize=18, weight=1)
        frame.rowconfigure(1, weight=0)
        frame.columnconfigure(0, minsize=80, weight=1) 
        frame.columnconfigure(1, weight=0) 
        frame.columnconfigure(2, weight=0) 
        frame.columnconfigure(3, weight=0)
        frame.columnconfigure(4, weight=1)
        
        return frame
    
    # executes period command
    def on_execute_period_command(self):
        pass   

# add record tab
class add_tab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.add_form = RecordForm(self,
            form_title="Add Record Preview"
        )
        self.add_form.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )
                 
# delete record tab
class delete_tab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        DeleteRecord(self).pack(
            fill="both", expand=True,
            padx=10, pady=10
        )
        
# update record tab
class update_tab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    
        self.update_form = RecordForm(
            self,
            form_title="Update Record Preview"
            )
        self.update_form.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )

