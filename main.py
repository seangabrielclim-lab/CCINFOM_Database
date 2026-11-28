import customtkinter as ctk
from frontend import THEMES as themes

from frontend.frames.record_table import RecordTable
from frontend.frames.record_form import RecordForm
from frontend.frames.report_frame import ReportFrame


class DemoApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("PharmaFlow - GUI Preview")
        self.geometry("1280x800")
        self.minsize(900, 600)
        self.configure(fg_color=themes.THEME_BG)

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

        # Main tabs
        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(
            row=1, column=1,
            sticky="nsew", padx=10, pady=10
        )

        sections = [
            "Manage Records",
            "Generate Reports"
        ]

        for section in sections:
            self.tabs.add(section)

            ctk.CTkButton(
                self.sidebar,
                text=section,
                width=180,
                height=45,
                fg_color="#4f4f4f",
                command=lambda p=section: self.tabs.set(p)
            ).pack(padx=10, pady=5)

        # Record management preview
        self.record_tabs = ctk.CTkTabview(
            self.tabs.tab("Manage Records")
        )
        self.record_tabs.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )

        for action in [
            "View/Filter",
            "Add",
            "Update",
            "Delete"
        ]:
            self.record_tabs.add(action)

        # View/Filter preview
        self.table = RecordTable(
            self.record_tabs.tab("View/Filter")
        )
        self.table.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )

        # Add form preview
        self.add_form = RecordForm(
            self.record_tabs.tab("Add"),
            form_title="Add Record Preview"
        )
        self.add_form.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )

        # Update form preview
        self.update_form = RecordForm(
            self.record_tabs.tab("Update"),
            form_title="Update Record Preview"
        )
        self.update_form.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )

        # Delete confirmation preview
        delete_tab = self.record_tabs.tab("Delete")

        ctk.CTkLabel(
            delete_tab,
            text="Delete Record Preview",
            font=("Helvetica", 22, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            delete_tab,
            text="Sample Record: 001"
        ).pack(pady=10)

        ctk.CTkLabel(
            delete_tab,
            text="Are you sure you want to delete this record?"
        ).pack(pady=10)

        ctk.CTkButton(
            delete_tab,
            text="Confirm Delete",
            fg_color="#c0392b",
            state="disabled"
        ).pack(pady=10)

        ctk.CTkButton(
            delete_tab,
            text="Cancel",
            fg_color="#585858",
            command=lambda: self.record_tabs.set("View/Filter")
        ).pack(pady=10)

        # Report preview
        self.report = ReportFrame(
            self.tabs.tab("Generate Reports")
        )
        self.report.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = DemoApp()
    app.mainloop()