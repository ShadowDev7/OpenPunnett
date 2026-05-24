import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("OpenPunnett")
        self.geometry("800x400")
        
        self.grid_columnconfigure(0, weight=1)
        # Title
        self.label = ctk.CTkLabel(self, text="Welcome to the OpenPunnett Calculator!")
        self.label.grid(row=0, 
                        column=0, 
                        padx=20, 
                        pady=20
                        )
        # Parent1
        self.entry1 = ctk.CTkEntry(self, placeholder_text="Parent 1 Genotype (e.g. Aa)")
        self.entry1.grid(row=2, 
                         column=0, 
                         padx=20, 
                         pady=10
                    )
        # Parent2
        self.entry2 = ctk.CTkEntry(self, placeholder_text="Parent 2 Genotype (e.g. Aa)")
        self.entry2.grid(row=3, 
                         column=0, 
                         padx=20, 
                         pady=10
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
                         pady=50
                    )


if __name__ == "__main__":
    app = App()
    app.mainloop()