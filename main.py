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
        self.configure(fg_color=themes.THEME_BG)

        self.minsize(900, 600)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        # Header
        self.header = ctk.CTkFrame(
            self, fg_color="#66a369", height=50
        )
        self.header.grid(
            row=0, column=0,
            columnspan=2,
            sticky="ew",
            padx=10, pady=10
        )

        ctk.CTkLabel(
            self.header,
            text="PharmaFlow - Academic Preview",
            font=(themes.THEME_FONT_FAMILY, 20, "bold"),
            text_color=themes.THEME_ACCENT_FG
        ).pack(side="left", padx=20, pady=10)

        self.sidebar = ctk.CTkFrame(
        self,
        width=180,
        fg_color=themes.THEME_BG
        )

        self.sidebar.grid(
        row=1, column=0,
        sticky="ns",
        padx=10, pady=10
        )

        ctk.CTkLabel(
        self.sidebar,
        text="Navigation",
        font=(themes.THEME_FONT_FAMILY, 16, "bold")
        ).pack(pady=15)

        for page in [
            "Sample Records",
            "Sample Form",
            "Sample Reports"
        ]:


            ctk.CTkButton(
                self.sidebar,
                text=page,
                width=160,
                height=45,
                fg_color="#4f4f4f",
                command=lambda p=page: self.tabs.set(p)
            ).pack(padx=10, pady=5)

        # Main content
        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(
            row=1, column=1,
            sticky="nsew",
            padx=10, pady=10
        )

        self.tabs.add("Sample Records")
        self.tabs.add("Sample Form")
        self.tabs.add("Sample Reports")

        # Table preview
        self.table = RecordTable(
            self.tabs.tab("Sample Records")
        )
        self.table.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )

        # Form preview
        self.form = RecordForm(
            self.tabs.tab("Sample Form")
        )
        self.form.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )

        # Report preview
        self.report = ReportFrame(
            self.tabs.tab("Sample Reports")
        )
        self.report.pack(
            fill="both", expand=True,
            padx=10, pady=10
        )


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = DemoApp()
    app.mainloop()