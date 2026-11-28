import customtkinter as ctk


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
                "Sample Report C"
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
            self, text="Select a sample report."
        )
        self.status.grid(
            row=2, column=0,
            sticky="w", padx=20
        )

        self.results = ctk.CTkTextbox(self)
        self.results.grid(
            row=3, column=0,
            sticky="nsew", padx=20, pady=20
        )
        self.results.configure(state="disabled")

    def generate_preview(self):

        selected = self.report_type.get()

        self.results.configure(state="normal")
        self.results.delete("1.0", "end")

        self.results.insert(
            "end",
            f"{selected}\n"
            "========================\n\n"
            "Fictional Report Preview\n\n"
            "Sample A: 10\n"
            "Sample B: 20\n"
            "Sample C: 30\n\n"
            "Total: 60\n"
        )

        self.results.configure(state="disabled")

        self.status.configure(
            text="Sample preview displayed.",
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