import customtkinter as ctk
from tkinter import ttk


class ReportFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        self.title = ctk.CTkLabel(
            self,
            text="Generate Reports",
            font=("Helvetica", 22, "bold")
        )
        self.title.grid(
            row=0, column=0,
            sticky="w", padx=20, pady=20
        )

        self.controls = ctk.CTkFrame(self)
        self.controls.grid(
            row=1, column=0,
            sticky="ew", padx=20, pady=10
        )

        self.report_type = ctk.CTkOptionMenu(
            self.controls,
            values=[
                "Sample Report A",
                "Sample Report B",
                "Sample Report C",
                "Sample Report D",
                "Sample Report E",
                "Sample Report F",
                "Sample Report G"
            ]
        )
        self.report_type.pack(
            side="left", padx=10, pady=10
        )

        self.generate_button = ctk.CTkButton(
            self.controls,
            text="Preview Report",
            command=self.generate_preview
        )
        self.generate_button.pack(
            side="left", padx=10
        )

        self.status = ctk.CTkLabel(
            self,
            text="Select a sample report."
        )
        self.status.grid(
            row=2, column=0,
            sticky="w", padx=20
        )

        self.results = ttk.Treeview(
            self,
            columns=("item", "value"),
            show="headings"
        )

        self.results.heading(
            "item", text="Sample Item"
        )
        self.results.heading(
            "value", text="Value"
        )

        self.results.column("item", width=300)
        self.results.column("value", width=150)

        self.results.grid(
            row=3, column=0,
            sticky="nsew",
            padx=20, pady=20
        )

    def generate_preview(self):
        selected = self.report_type.get()

        for item in self.results.get_children():
            self.results.delete(item)

        sample_data = [
            ("Sample A", 10),
            ("Sample B", 20),
            ("Sample C", 30),
            ("Total", 60)
        ]

        for row in sample_data:
            self.results.insert(
                "", "end", values=row
            )

        self.status.configure(
            text=f"{selected} - Fictional Preview",
            text_color="#66a369"
        )


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    root.title("Report Preview")
    root.geometry("900x600")

    report = ReportFrame(root)
    report.pack(
        fill="both", expand=True,
        padx=20, pady=20
    )

    root.mainloop()