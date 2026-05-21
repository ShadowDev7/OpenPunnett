import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Punnett Square Calculator")
        self.geometry("400x300")
        
        self.grid_columnconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self, text="Welcome to the Punnett Square Calculator!")
        self.label.grid(row=0, column=0, padx=20, pady=20)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()