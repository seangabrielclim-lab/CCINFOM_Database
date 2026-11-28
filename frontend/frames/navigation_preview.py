import customtkinter as ctk


class NavigationPreview(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#363636")

        self.pack(fill="both", expand=True)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(
            self, width=180
        )
        self.sidebar.grid(
            row=0, column=0,
            sticky="ns", padx=10, pady=10
        )

        self.content = ctk.CTkFrame(
            self, fg_color="#ffffff"
        )
        self.content.grid(
            row=0, column=1,
            sticky="nsew", padx=10, pady=10
        )

        # Fictional demonstration screens
        pages = [
            "Overview",
            "Sample Records",
            "Sample Reports",
            "Settings"
        ]

        for page in pages:
            button = ctk.CTkButton(
                self.sidebar,
                text=page,
                width=160,
                height=45,
                command=lambda p=page: self.show_page(p)
            )
            button.pack(padx=10, pady=5)

        self.show_page("Overview")

    def show_page(self, page):

        for widget in self.content.winfo_children():
            widget.destroy()

        title = ctk.CTkLabel(
            self.content,
            text=page,
            text_color="#1a1a1a",
            font=("Helvetica", 22, "bold")
        )
        title.pack(anchor="w", padx=20, pady=20)

        description = ctk.CTkLabel(
            self.content,
            text=f"{page} preview",
            text_color="#585858"
        )
        description.pack(anchor="w", padx=20)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    root.title("Navigation Preview")
    root.geometry("1000x650")

    app = NavigationPreview(root)

    root.mainloop()