# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
# Requires CustomTkinter:  pip install customtkinter
import customtkinter as ctk
from tkinter import messagebox
from database import init_database


class ScrollableFrame(ctk.CTkFrame):
    """A frame that scrolls. Put your widgets in `.body`, not in this."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._canvas = ctk.CTkCanvas(self, highlightthickness=0, bg="#363636")
        self._bar = ctk.CTkScrollbar(self, orientation="vertical", command=self._on_scrollbar)
        self._canvas.configure(yscrollcommand=self._bar.set)
        self._bar.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        self.body = ctk.CTkFrame(self._canvas, fg_color="transparent")
        self._window = self._canvas.create_window((0, 0), window=self.body, anchor="nw")

        self.body.bind("<Configure>", self._on_body)
        self._canvas.bind("<Configure>", self._on_canvas)

        self._canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self._canvas.bind_all("<Button-4>", self._on_mousewheel)
        self._canvas.bind_all("<Button-5>", self._on_mousewheel)

    def _on_body(self, _event=None):
        # Clamp scrollregion to (0, 0) and at least the canvas height so it never overscrolls
        width = max(self.body.winfo_reqwidth(), self._canvas.winfo_width())
        height = max(self.body.winfo_reqheight(), self._canvas.winfo_height())
        self._canvas.configure(scrollregion=(0, 0, width, height))

    def _on_canvas(self, event):
        self._canvas.itemconfig(self._window, width=event.width)
        self._on_body()

    def _on_scrollbar(self, *args):
        top, bottom = self._canvas.yview()
        if top <= 0.0 and bottom >= 1.0:
            return
        if args[0] == "moveto" and float(args[1]) < 0.0:
            self._canvas.yview_moveto(0.0)
            return
        self._canvas.yview(*args)

    def _on_mousewheel(self, event):
        top, bottom = self._canvas.yview()
        # If all buttons fit inside the maximized window, disable scrolling completely
        if top <= 0.0 and bottom >= 1.0:
            self._canvas.yview_moveto(0.0)
            return

        if event.num == 4 or event.delta > 0:
            if top > 0.0:
                self._canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            if bottom < 1.0:
                self._canvas.yview_scroll(1, "units")


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
    def __init__(self, master, login):
        root = ctk.CTkToplevel(master)
        self.root = root
        root.title("PharmaFlow")
        root.geometry("1200x800")       
        apply_theme(root)
        self.db = None
        self.login = login
        
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.frame15 = ctk.CTkFrame(root, border_width=2, fg_color=THEME_BG, width=420, height=330)
        self.frame15.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.frame2 = ctk.CTkFrame(self.frame15, fg_color="#66a369", border_width=2, corner_radius=1, width=520, height=50)
        self.frame2.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=4, pady=4)

        self.logout = ctk.CTkButton(self.frame2, text="Logout", command=self.on_logout, fg_color="#e77474", text_color=THEME_ACCENT_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=70, height=20)
        self.logout.grid(row=0, column=1, sticky="nsew", padx=4, pady=4)

        self.label3 = ctk.CTkLabel(self.frame2, text="PharmaFlow", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"), width=170, height=30)
        self.label3.grid(row=0, column=0, sticky="w", padx=4, pady=4)

        self.notebook4 = ctk.CTkTabview(self.frame15, fg_color=THEME_BG, width=370, height=310)
        self.notebook4.add("Manage Record")
        self.notebook4.add("Generate Report")
        self.notebook4.grid(row=1, column=3, rowspan=4, sticky="nsew", padx=4, pady=4)

        self.frame16 = ctk.CTkFrame(self.notebook4.tab("Manage Record"), fg_color="#ffffff", border_width=2, width=370, height=270)
        self.frame16.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.frame19 = ctk.CTkFrame(self.notebook4.tab("Generate Report"), fg_color="#ffffff", border_width=2, width=370, height=270)
        self.frame19.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.scrollframe5 = ScrollableFrame(self.frame15, width=130, height=270)
        self.scrollframe5.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=4, pady=4)

        self.label10 = ctk.CTkLabel(self.frame15, text="Records", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"), width=90, height=20)
        self.label10.grid(row=2, column=1, sticky="nsew", padx=4, pady=4)

        self.frame22 = ctk.CTkFrame(self.scrollframe5.body, border_width=2, fg_color=THEME_BG, width=130, height=270)
        self.frame22.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.drug = ctk.CTkButton(self.frame22, text="Drug Record", command=self.on_drug, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.drug.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)

        self.resupply = ctk.CTkButton(self.frame22, text="Resupply Record", command=self.on_resupply, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.resupply.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)

        self.customer = ctk.CTkButton(self.frame22, text="Customer Record", command=self.on_customer, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.customer.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)

        self.sales = ctk.CTkButton(self.frame22, text="Sales Record", command=self.on_sales, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.sales.grid(row=3, column=0, sticky="nsew", padx=4, pady=4)

        self.logistics = ctk.CTkButton(self.frame22, text="Logistics Record", command=self.on_logistics, fg_color="#4f4f4f", font=ctk.CTkFont(family="Helvetica", size=13, weight="bold"), text_color=THEME_ACCENT_FG, width=100, height=50)
        self.logistics.grid(row=4, column=0, sticky="nsew", padx=4, pady=4)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.frame15.columnconfigure(0, minsize=20, weight=0)
        self.frame15.columnconfigure(1, minsize=78, weight=0)
        self.frame15.columnconfigure(2, minsize=28, weight=0)
        self.frame15.columnconfigure(3, minsize=383, weight=1)
        self.frame15.columnconfigure(4, minsize=18, weight=0)
        self.frame15.rowconfigure(0, minsize=58, weight=0)
        self.frame15.rowconfigure(1, minsize=18, weight=0)
        self.frame15.rowconfigure(2, minsize=28, weight=0)
        self.frame15.rowconfigure(3, minsize=18, weight=0)
        self.frame15.rowconfigure(4, minsize=278, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=0)
        self.frame2.rowconfigure(0, weight=1)
        self.notebook4.tab("Manage Record").columnconfigure(0, weight=1)
        self.notebook4.tab("Manage Record").rowconfigure(0, weight=1)
        self.notebook4.tab("Generate Report").columnconfigure(0, weight=1)
        self.notebook4.tab("Generate Report").rowconfigure(0, weight=1)
        self.scrollframe5.body.columnconfigure(0, minsize=80, weight=1)
        self.scrollframe5.body.rowconfigure(0, minsize=278, weight=1)
        self.frame22.columnconfigure(0, weight=1)
        self.frame22.rowconfigure(0, minsize=58)
        self.frame22.rowconfigure(1, minsize=58)
        self.frame22.rowconfigure(2, minsize=58)
        self.frame22.rowconfigure(3, minsize=58)
        self.frame22.rowconfigure(4, minsize=65)

    def on_closing(self):
        if self.db is not None:
            LogoutBeforeClosing(self.root)

    def on_logout(self):
        
        if self.db is not None:
            try:
                self.db.close()
            except Exception as e:
                print(f"failed to connect. {e}")
            
            self.db = None
        
        self.root.destroy()
        self.login.root.deiconify()

    def on_drug(self):
        pass

    def on_resupply(self):
        pass

    def on_customer(self):
        pass

    def on_sales(self):
        pass

    def on_logistics(self):
        pass
    
    def set_db(self, db):
        self.db = db

class Login:
    def __init__(self, root):
        self.root = root
        root.title("Login")
        root.geometry("520x380")
        apply_theme(root)
        
        self.password = ctk.CTkEntry(root, fg_color=THEME_FIELD_BG, text_color=THEME_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), width=350, height=30, show='*')
        self.password.grid(row=2, column=1, columnspan=5, sticky="w", padx=4, pady=4)

        self.label2 = ctk.CTkLabel(root, text="Password", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=12), width=90, height=26)
        self.label2.grid(row=1, column=1, sticky="w", padx=4, pady=4)

        self.label3 = ctk.CTkLabel(root, text="PharmaFlow", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"), width=170, height=40)
        self.label3.grid(row=0, column=1, columnspan=3, sticky="w", padx=4, pady=4)

        self.login = ctk.CTkButton(root, text="Login", command=self.on_login, fg_color="#79a267", font=ctk.CTkFont(family="Helvetica", size=10), text_color=THEME_ACCENT_FG, width=90, height=30)
        self.login.grid(row=3, column=1, sticky="w", padx=4, pady=4)

        self.status = ctk.CTkLabel(root, text="", text_color="#ffffff", font=ctk.CTkFont(family="Helvetica", size=12), width=90, height=26)
        self.status.grid(row=4, column=1, sticky="w", padx=4, pady=4)

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=0)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, minsize=150)
        root.rowconfigure(1, minsize=34)
        root.rowconfigure(2, minsize=38)
        root.rowconfigure(3, minsize=38)
        root.rowconfigure(4, minsize=34)
        
    def open_PharmaFlow(self):
        return PharmaFlow(self.root, self)

    def on_login(self):
        password = self.password.get()
        db, msg = init_database(password)
        
        if (db==None):
            self.password.delete(0, "end")
            self.status.configure(text=msg)
        else:
            self.password.delete(0, "end")
            self.status.configure(text="")
            self.root.withdraw()
            pharmaflow = self.open_PharmaFlow()
            pharmaflow.set_db(db)
            
class LogoutBeforeClosing:
    def __init__(self, master):
        root = ctk.CTkToplevel(master)
        self.root = root
        root.title("Logout Before Closing")
        root.geometry("520x380")
        apply_theme(root)
        
        root.transient(master)
        root.grab_set()

        self.label1 = ctk.CTkLabel(root, text="Logout before closing the application", wraplength=340, text_color="#fffafa", font=ctk.CTkFont(family="Helvetica", size=23, weight="bold"), width=340, height=190)
        self.label1.place(x=90, y=20)

        self.button1 = ctk.CTkButton(root, text="Return", command=self.on_button1, fg_color="#e12d2d", font=ctk.CTkFont(family="Helvetica", size=12, weight="bold"), text_color=THEME_ACCENT_FG, width=150, height=50)
        self.button1.place(x=185, y=210)

    def on_button1(self):
        self.root.destroy()
        pass


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = Login(root)
    root.mainloop()
