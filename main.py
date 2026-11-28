# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
# Requires CustomTkinter:  pip install customtkinter
# Requires tkcalendar: pip install tkcalendars

import customtkinter as ctk
from database import init_database
from frontend import THEMES as themes

# record frames
from frontend.frames.record_frames.drug_record_frame import drug_record_frame
from frontend.frames.record_frames.resupply_record_frame import resupply_record_frame
from frontend.frames.record_frames.sales_record_frame import sales_record_frame
from frontend.frames.record_frames.customer_record_frame import customer_record_frame
from frontend.frames.record_frames.logistics_record_frame import logistics_record_frame
# report frames
from frontend.frames.report_frames.sales_report_frame import sales_report_frame
from frontend.frames.report_frames.logistics_report_frame import logistics_report_frame
from frontend.frames.report_frames.supply_report_frame import supply_report_frame
from frontend.frames.report_frames.transportation_report_frame import transportation_report_frame
from frontend.frames.report_frames.delivery_report_frame import delivery_report_frame
from frontend.frames.report_frames.demand_report_frame import demand_report_frame
from frontend.frames.report_frames.destination_report_frame import destination_report_frame

THEME_BG = themes.THEME_BG
THEME_FG = themes.THEME_FG
THEME_ACCENT = themes.THEME_ACCENT
THEME_ACCENT_FG = themes.THEME_ACCENT_FG
THEME_FIELD_BG = themes.THEME_FIELD_BG
THEME_FONT_FAMILY = themes.THEME_FONT_FAMILY
THEME_FONT_SIZE = themes.THEME_FONT_SIZE

class PharmaFlow(ctk.CTkToplevel):
    def __init__(self, master,login):
        super().__init__(master)
        self.title("PharmaFlow - GUI Preview")
        self.geometry("1280x800")
        self.minsize(900, 600)
        self.configure(fg_color=themes.THEME_BG)
        apply_theme(self)
        
        self.db = None
        self.login = login
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        # Header
        self.header = ctk.CTkFrame(
            self, fg_color="#66a369", height=50
        )
        self.header.grid(
            row=0, column=0, columnspan=2,
            sticky="ew", padx=10, pady=10
        )

        ctk.CTkLabel(
            self.header,
            text="PharmaFlow - Academic Preview",
            font=(themes.THEME_FONT_FAMILY, 20, "bold"),
            text_color=themes.THEME_ACCENT_FG
        ).pack(side="left", padx=20, pady=10)
        
        self.logout = ctk.CTkButton(
            self.header, 
            text="Logout", command=self.on_logout, fg_color="#e77474", 
            text_color=THEME_ACCENT_FG, font=ctk.CTkFont(family=THEME_FONT_FAMILY, size=THEME_FONT_SIZE), 
            width=70, height=30
        )
        
        self.logout.pack(side="right", padx=20, pady=10)

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self, width=180,
            fg_color=themes.THEME_BG
        )
        self.sidebar.grid(
            row=1, column=0,
            sticky="ns", padx=10, pady=10
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Navigation",
            font=("Helvetica", 16, "bold")
        ).pack(pady=15)
        
        ctk.CTkButton(
            self.sidebar,
            text="Manage Record",
            width=180,
            height=45,
            fg_color="#4f4f4f",
            command=lambda: self.show_management_tab("Records")
        ).pack(padx=10, pady=5)
        
        ctk.CTkButton(
            self.sidebar,
            text="Generate Report",
            width=180,
            height=45,
            fg_color="#4f4f4f",
            command=lambda: self.show_management_tab("Reports")
        ).pack(padx=10, pady=5)

        # Main tabs
        self.management_tabs = {
            "Records" : self.record_tabs(),
            "Reports" : self.report_tabs()
        } 
        
        for tabs in self.management_tabs.values():
            tabs.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
            tabs.grid_remove()
        
        # shows records tab as the default tab  
        self.management_tabs["Records"].grid() 
      
    # creates record tabs  
    def record_tabs(self):
        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(
        row=1, column=1,
        sticky="nsew", padx=10, pady=10
        )
                
        sections = [
            "Drug Record",
            "Sales Record",
            "Customer Record",
            "Resupply Record",
            "Logistics Record"
        ]
        
        # Record management preview
        for section in sections:
            self.tabs.add(section)
        
        self.drug_record = ctk.CTkTabview(self.tabs.tab("Drug Record"))    
        self.sales_record = ctk.CTkTabview(self.tabs.tab("Sales Record"))
        self.customer_record = ctk.CTkTabview(self.tabs.tab("Customer Record"))
        self.resupply_record = ctk.CTkTabview(self.tabs.tab("Resupply Record"))
        self.logistics_record = ctk.CTkTabview(self.tabs.tab("Logistics Record"))
        
        record_frames = [
            self.drug_record,
            self.sales_record,
            self.customer_record,
            self.resupply_record,
            self.logistics_record
        ]
        
        for frame in record_frames:
            for action in ["View/Filter","Add","Update","Delete"]:
                frame.add(action)
            frame.pack(fill="both", expand=True,padx=10, pady=10)
           
        # adding content into each record 
        drug_record_frame(self.drug_record, self.db)
        resupply_record_frame(self.resupply_record, self.db)
        customer_record_frame(self.customer_record, self.db)
        sales_record_frame(self.sales_record, self.db)
        logistics_record_frame(self.logistics_record, self.db)
            
        return self.tabs
        
    # creates report tabs    
    def report_tabs(self):
        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(
        row=1, column=1,
        sticky="nsew", padx=10, pady=10
        )
                
        sections = [
            "Sales Report",
            "Logistics Report",
            "Supply Distribution Report",
            "Transportation Usage Report",
            "Delivery Status Report",
            "Product Demand Report",
            "Destination Report"
        ]
        
        # Record management preview
        for section in sections:
            self.tabs.add(section)
        
        
        # adding content to the report frames
        sales_report_frame(self.tabs.tab("Sales Report"), self.db).pack(fill="both", expand=True, padx=10, pady=10)
        logistics_report_frame(self.tabs.tab("Logistics Report"), self.db).pack(fill="both", expand=True, padx=10, pady=10)
        supply_report_frame(self.tabs.tab("Supply Distribution Report"), self.db).pack(fill="both", expand=True, padx=10, pady=10)
        transportation_report_frame(self.tabs.tab("Transportation Usage Report"), self.db).pack(fill="both", expand=True, padx=10, pady=10)
        delivery_report_frame(self.tabs.tab("Delivery Status Report"), self.db).pack(fill="both", expand=True, padx=10, pady=10)
        demand_report_frame(self.tabs.tab("Product Demand Report"), self.db).pack(fill="both", expand=True, padx=10, pady=10)
        destination_report_frame(self.tabs.tab("Destination Report"), self.db).pack(fill="both", expand=True, padx=10, pady=10)
        
        return self.tabs
         
    # shows what manage tab we currently are in
    def show_management_tab(self, selected_tab):
        
        for tabs in self.management_tabs.values():
            tabs.grid_remove()
            
        self.management_tabs[selected_tab].grid()
        
    # prevents application closing when user is not logged out
    def on_closing(self):
        if self.db is not None:
            LogoutBeforeClosing(self)
    
    # logs out of the application and closes the connection to the database
    def on_logout(self):
        if self.db is not None:
            try:
                self.db.close()
            except Exception as e:
                print(f"failed to connect. {e}")
                
            self.db = None
            
        self.destroy()
        self.login.root.deiconify()
        
    def set_db(self, db):
        self.db = db


# This is the login frame. 
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
            
# This frame shows the warning that the user needs to logout before exiting         
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

def apply_theme(root):
    root.configure(fg_color=THEME_BG)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = Login(root)
    root.mainloop()