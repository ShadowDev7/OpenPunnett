import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Punnett Square Calculator")
        self.geometry("400x300")
        
        self.grid_columnconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self, text="Welcome to the Punnett Square Calculator!")
        self.label.grid(row=0, 
                        column=0, 
                        padx=20, 
                        pady=20
                        )

        self.button = ctk.CTkButton(self, 
                                    text="Calculate", 
                                    command=lambda: self.button.configure(text="Calculating..."),
                                    height=40,
                                    width=120,
                                    font=("Arial", 14),
                                    text_color="black",
                                    fg_color="white",
                                    hover_color="gray",
                                    corner_radius=20,
                                )
        
        self.button.grid(row=1, 
                         column=0,
                         pady=20
                    )


if __name__ == "__main__":
    app = App()
    app.mainloop()