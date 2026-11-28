import customtkinter as ctk


class RecordForm(ctk.CTkFrame):

    def __init__(self, master, form_title="Sample Record Form", **kwargs):
        super().__init__(master, **kwargs)

        self.columnconfigure(1, weight=1)
        self.entries = {}

        title = ctk.CTkLabel(
            self,
            text=form_title,
            font=("Helvetica", 22, "bold")
        )
        title.grid(
            row=0, column=0, columnspan=2,
            sticky="w", padx=20, pady=20
        )

        fields = [
            "Record ID",
            "Name",
            "Description"
        ]

        for i, field in enumerate(fields, start=1):

            label = ctk.CTkLabel(self, text=field)
            label.grid(
                row=i, column=0,
                sticky="w", padx=20, pady=10
            )

            entry = ctk.CTkEntry(self, height=35)
            entry.grid(
                row=i, column=1,
                sticky="ew", padx=20, pady=10
            )

            self.entries[field] = entry

        self.button_frame = ctk.CTkFrame(
            self, fg_color="transparent"
        )
        self.button_frame.grid(
            row=4, column=0, columnspan=2,
            pady=20
        )

        self.preview_button = ctk.CTkButton(
            self.button_frame,
            text="Preview",
            command=self.preview
        )
        self.preview_button.pack(side="left", padx=5)

        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="Clear",
            fg_color="#585858",
            command=self.clear
        )
        self.clear_button.pack(side="left", padx=5)

        self.status = ctk.CTkLabel(self, text="")
        self.status.grid(
            row=5, column=0, columnspan=2,
            pady=10
        )

    def preview(self):
        if any(
            not entry.get().strip()
            for entry in self.entries.values()
        ):
            self.status.configure(
                text="Please complete all fields.",
                text_color="#e77474"
            )
            return

        self.status.configure(
            text="Preview successful. No data saved.",
            text_color="#66a369"
        )

    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, "end")

        self.status.configure(text="")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    root.title("Record Form Preview")
    root.geometry("800x500")

    form = RecordForm(root)
    form.pack(
        fill="both", expand=True,
        padx=20, pady=20
    )

    root.mainloop()