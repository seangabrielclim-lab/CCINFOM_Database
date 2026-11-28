# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
# Requires CustomTkinter:  pip install customtkinter
import customtkinter as ctk
import tkinter as tk


class ScrollableFrame(ctk.CTkFrame):
    """A frame that scrolls. Put your widgets in `.body`, not in this."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._canvas = ctk.CTkCanvas(
            self,
            highlightthickness=0,
            bg=THEME_BG
        )
        self._bar = ctk.CTkScrollbar(self, orientation="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self._bar.set)
        self._bar.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)
        self.body = ctk.CTkFrame(self._canvas)
        self._window = self._canvas.create_window((0, 0), window=self.body, anchor="nw")
        # The scroll region follows whatever size the body is given.
        self.body.bind("<Configure>", self._on_body)

    def _on_body(self, _event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))


THEME_BG = "#363636"
THEME_FG = "#1a1a1a"
THEME_ACCENT = "#2a7de1"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#ffffff"
THEME_FONT_FAMILY = "Helvetica"
THEME_FONT_SIZE = 10


def apply_theme(root):
    """Apply the project theme to a window. CustomTkinter styles per widget,
    so the widgets themselves carry the rest of the colours."""
    root.configure(fg_color=THEME_BG)


class PharmaFlow:
    def __init__(self, root):
        self.root = root
        root.title("PharmaFlow")
        root.geometry("1280x800")
        apply_theme(root)

        self.main_frame = ctk.CTkFrame(root, border_width=2, fg_color=THEME_BG, width=1280, height=750)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="#66a369", border_width=2, corner_radius=1, width=1280, height=50)
        self.header_frame.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=4, pady=4)

        self.btn_logout = ctk.CTkButton(self.header_frame, text="Logout", command=self.on_btn_logout, fg_color="#e77474", text_color=THEME_ACCENT_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=110, height=30)
        self.btn_logout.grid(row=0, column=1, sticky="e", padx=12, pady=4)

        self.label3 = ctk.CTkLabel(self.header_frame, text="PharmaFlow", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"), width=170, height=30)
        self.label3.grid(row=0, column=0, sticky="w", padx=4, pady=4)

        self.main_notebook = ctk.CTkTabview(self.main_frame, fg_color=THEME_BG, width=800, height=550)
        self.main_notebook.add("Manage Records")
        self.main_notebook.add("Generate Reports")
        self.main_notebook.grid(row=1, column=3, rowspan=5, sticky="nsew", padx=4, pady=4)

        self.records_content_frame = ctk.CTkFrame(self.main_notebook.tab("Manage Records"), fg_color="#ffffff", border_width=2, width=780, height=500)
        self.records_content_frame.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.frame19 = ctk.CTkFrame(self.main_notebook.tab("Generate Reports"), fg_color="#ffffff", border_width=2, width=370, height=270)
        self.frame19.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.scrollframe5 = ScrollableFrame(self.main_frame, width=130, height=270)
        self.scrollframe5.grid(row=4, column=0, columnspan=3, sticky="w", padx=4, pady=4)

        self.label10 = ctk.CTkLabel(self.main_frame, text="Records", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"), width=90, height=20)
        self.label10.grid(row=2, column=1, sticky="w", padx=4, pady=4)

        self.frame22 = ctk.CTkFrame(self.scrollframe5.body, border_width=2, fg_color=THEME_BG, width=130, height=270)
        self.frame22.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.button14 = ctk.CTkButton(self.frame22, text="Drug", command=self.on_button14, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.button14.grid(row=0, column=0, sticky="w", padx=4, pady=4)

        self.button15 = ctk.CTkButton(self.frame22, text="Resupply", command=self.on_button15, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.button15.grid(row=1, column=0, sticky="w", padx=4, pady=4)

        self.button16 = ctk.CTkButton(self.frame22, text="Customer", command=self.on_button16, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.button16.grid(row=2, column=0, sticky="w", padx=4, pady=4)

        self.button17 = ctk.CTkButton(self.frame22, text="Sales", command=self.on_button17, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.button17.grid(row=3, column=0, sticky="w", padx=4, pady=4)

        self.button18 = ctk.CTkButton(self.frame22, text="Logistics", command=self.on_button18, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.button18.grid(row=4, column=0, sticky="w", padx=4, pady=4)

        self.button19 = ctk.CTkButton(self.records_content_frame, text="Button", command=self.on_button19, fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=96, height=32)
        self.button19.grid(row=0, column=0, sticky="w", padx=4, pady=4)

        self.button20 = ctk.CTkButton(self.records_content_frame, text="Button", command=self.on_button20, fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=96, height=32)
        self.button20.grid(row=0, column=1, sticky="w", padx=4, pady=4)

        self.button21 = ctk.CTkButton(self.records_content_frame, text="Button", command=self.on_button21, fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=96, height=32)
        self.button21.grid(row=0, column=2, sticky="w", padx=4, pady=4)

        self.main_frame.columnconfigure(0, minsize=20, weight=0)
        self.main_frame.columnconfigure(1, minsize=110, weight=0)
        self.main_frame.columnconfigure(2, minsize=20, weight=0)
        self.main_frame.columnconfigure(3, weight=1)
        self.main_frame.columnconfigure(4, minsize=10, weight=0)

        self.main_frame.rowconfigure(0, minsize=58, weight=0)
        self.main_frame.rowconfigure(1, minsize=18, weight=0)
        self.main_frame.rowconfigure(2, minsize=28, weight=0)
        self.main_frame.rowconfigure(3, minsize=18, weight=0)
        self.main_frame.rowconfigure(4, weight=1)
        self.main_frame.rowconfigure(5, weight=1)
        self.header_frame.columnconfigure(0, minsize=178, weight=1)
        self.header_frame.columnconfigure(1, minsize=118, weight=0)
        self.header_frame.rowconfigure(0, minsize=38)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.main_notebook.tab("Manage Records").columnconfigure(0, weight=1)
        self.main_notebook.tab("Manage Records").rowconfigure(0, weight=1)
        self.main_notebook.tab("Generate Reports").columnconfigure(0, minsize=378, weight=1)
        self.main_notebook.tab("Generate Reports").rowconfigure(0, minsize=278, weight=1)
        self.scrollframe5.body.columnconfigure(0, minsize=138, weight=1)
        self.scrollframe5.body.rowconfigure(0, minsize=278, weight=1)
        self.frame22.columnconfigure(0, minsize=108)
        self.frame22.rowconfigure(0, minsize=58)
        self.frame22.rowconfigure(1, minsize=58)
        self.frame22.rowconfigure(2, minsize=58)
        self.frame22.rowconfigure(3, minsize=58)
        self.frame22.rowconfigure(4, minsize=65)
        self.records_content_frame.columnconfigure(0, minsize=104)
        self.records_content_frame.columnconfigure(1, minsize=104)
        self.records_content_frame.columnconfigure(2, minsize=104)
        self.records_content_frame.rowconfigure(0, minsize=40)

        self.scrollframe5.body.configure(width=114, height=400)

    def open_login(self):
        return Login(self.root)

    def open_logout_before_closing(self):
        return LogoutBeforeClosing(self.root)

    def open_drug_record_frame(self):
        return DrugRecordFrame(self.root)

    def on_btn_logout(self):
        pass

    def on_button14(self):
        pass

    def on_button15(self):
        pass

    def on_button16(self):
        pass

    def on_button17(self):
        pass

    def on_button18(self):
        pass

    def on_button19(self):
        pass

    def on_button20(self):
        pass

    def on_button21(self):
        pass


class Login:
    def __init__(self, master):
        root = ctk.CTkToplevel(master)
        self.root = root
        root.title("Login")
        root.geometry("520x380")
        apply_theme(root)

        self.password = ctk.CTkEntry(root, fg_color=THEME_FIELD_BG, text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=350, height=30)
        self.password.grid(row=2, column=0, columnspan=5, sticky="ew", padx=4, pady=4)

        self.label2 = ctk.CTkLabel(root, text="Password", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=12), width=90, height=26)
        self.label2.grid(row=1, column=0, sticky="w", padx=4, pady=4)

        self.label3 = ctk.CTkLabel(root, text="PharmaFlow", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"), width=170, height=40)
        self.label3.grid(row=0, column=1, columnspan=3, sticky="w", padx=4, pady=4)

        self.login = ctk.CTkButton(root, text="Login", command=self.on_login, fg_color="#79a267", font=ctk.CTkFont(family="Helvetica", size=10), text_color=THEME_ACCENT_FG, width=90, height=30)
        self.login.grid(row=3, column=4, sticky="w", padx=4, pady=4)

        self.status = ctk.CTkLabel(root, text="", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=12), width=90, height=26)
        self.status.grid(row=4, column=2, sticky="w", padx=4, pady=4)

        root.columnconfigure(0, minsize=98, weight=1)
        root.columnconfigure(1, minsize=53, weight=1)
        root.columnconfigure(2, minsize=98, weight=1)
        root.columnconfigure(3, minsize=48, weight=1)
        root.columnconfigure(4, minsize=98, weight=1)
        root.rowconfigure(0, minsize=48)
        root.rowconfigure(1, minsize=34)
        root.rowconfigure(2, minsize=38)
        root.rowconfigure(3, minsize=38)
        root.rowconfigure(4, minsize=34)

    def on_login(self):
        pass


class LogoutBeforeClosing:
    def __init__(self, master):
        root = ctk.CTkToplevel(master)
        self.root = root
        root.title("Logout Before Closing")
        root.geometry("520x380")
        apply_theme(root)

        self.label1 = ctk.CTkLabel(root, text="Logout before closing the application", wraplength=340, text_color="#fffafa", font=ctk.CTkFont(family="Helvetica", size=23, weight="bold"), width=340, height=190)
        self.label1.place(x=90, y=20)

        self.button1 = ctk.CTkButton(root, text="Return", command=self.on_button1, fg_color="#e12d2d", font=ctk.CTkFont(family="Helvetica", size=12, weight="bold"), text_color=THEME_ACCENT_FG, width=150, height=50)
        self.button1.place(x=185, y=210)

    def on_button1(self):
        pass


class DrugRecordFrame:
    def __init__(self, master):
        root = ctk.CTkToplevel(master)
        self.root = root
        root.title("drug_record_frame")
        root.geometry("520x380")
        apply_theme(root)

        self.optionmenu4_var = tk.StringVar()
        self.optionmenu4_var.set("Category")

        self.frame1 = ctk.CTkFrame(root, fg_color="#ffffff", border_width=2, width=370, height=270)
        self.frame1.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.record_functions = ctk.CTkTabview(self.frame1, fg_color=THEME_BG, width=370, height=270)
        self.record_functions.add("View/Filter")
        self.record_functions.add("Add")
        self.record_functions.add("Delete")
        self.record_functions.add("Update")
        self.record_functions.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.frame2 = ctk.CTkFrame(self.record_functions.tab("View/Filter"), border_width=2, fg_color=THEME_BG, width=350, height=60)
        self.frame2.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.optionmenu4 = ctk.CTkOptionMenu(self.frame2, values=["Category", "Source Country", "Stock", "Period"], variable=self.optionmenu4_var, fg_color=THEME_ACCENT, text_color=THEME_ACCENT_FG, width=100, height=20)
        self.optionmenu4.grid(row=1, column=0, columnspan=2, sticky="w", padx=4, pady=4)

        self.frame3 = ctk.CTkFrame(self.frame2, border_width=2, fg_color=THEME_BG, width=210, height=60)
        self.frame3.grid(row=0, column=2, rowspan=3, sticky="nsew", padx=4, pady=4)

        self.label1 = ctk.CTkLabel(self.frame2, text="Filter by:", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), width=90, height=26)
        self.label1.grid(row=0, column=0, sticky="w", padx=4, pady=4)

        root.columnconfigure(0, minsize=378, weight=1)
        root.rowconfigure(0, minsize=278, weight=1)
        self.frame1.columnconfigure(0, minsize=378, weight=1)
        self.frame1.rowconfigure(0, minsize=278, weight=1)
        self.record_functions.tab("View/Filter").columnconfigure(0, minsize=358, weight=1)
        self.record_functions.tab("View/Filter").rowconfigure(0, minsize=68, weight=1)
        self.frame2.columnconfigure(0, minsize=98)
        self.frame2.columnconfigure(1, minsize=18)
        self.frame2.columnconfigure(2, minsize=218, weight=1)
        self.frame2.rowconfigure(0, minsize=34, weight=1)
        self.frame2.rowconfigure(1, minsize=28, weight=1)
        self.frame2.rowconfigure(2, minsize=22, weight=1)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = PharmaFlow(root)
    root.mainloop()
