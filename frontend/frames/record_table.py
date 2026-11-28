import customtkinter as ctk
from tkinter import ttk


class RecordTable(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        columns = ("id", "name", "description")

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings"
        )

        self.table.heading("id", text="Record ID")
        self.table.heading("name", text="Name")
        self.table.heading("description", text="Description")

        self.table.column("id", width=100)
        self.table.column("name", width=180)
        self.table.column("description", width=250)

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.table.yview
        )

        self.table.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.table.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        # Fictional preview data only
        self.table.insert("", "end", values=(
            "001", "Sample A", "Demo record"
        ))

        self.table.insert("", "end", values=(
            "002", "Sample B", "Demo record"
        ))


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Record Table Preview")
    root.geometry("800x500")

    table = RecordTable(root)
    table.pack(fill="both", expand=True, padx=20, pady=20)

    root.mainloop()