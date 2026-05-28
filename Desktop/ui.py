import customtkinter as ctk
from tkinter import messagebox

from logic import calculate, graphs

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("OpenPunnett")
        self.geometry("800x400")
        
        self.grid_columnconfigure(0, weight=1)
        # Title
        self.label = ctk.CTkLabel(self, text="Welcome to the OpenPunnett Calculator!", font=("Arial", 18))
        self.label.grid(row=0, 
                        column=0, 
                        padx=20, 
                        pady=20
                        )
        # Parent1
        self.entry1 = ctk.CTkEntry(self, placeholder_text="Parent 1 Genotype (e.g. Aa)", font=("Arial", 14))
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
                                    command=self.show_results,
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

    def show_results(self):
        parent1 = self.entry1.get().strip()
        parent2 = self.entry2.get().strip()

        if parent1 not in ["AA", "Aa", "aA", "aa"] or parent2 not in ["AA", "Aa", "aA", "aa"]:
            messagebox.showerror("Invalid Input", "Use AA, Aa, aA, or aa for both parents.")
            return

        results = calculate(parent1, parent2)
        genotype = results["genotype"]
        phenotype = results["phenotype"]

        self.label.configure(
            text=(
                f"Genotype: AA {genotype['AA']:.1f}%, "
                f"Aa {genotype['Aa']:.1f}%, aa {genotype['aa']:.1f}%\n"
                f"Phenotype: A {phenotype['A']:.1f}%, a {phenotype['a']:.1f}%"
            )
        )
        graphs(results)


if __name__ == "__main__":
    app = App()
    app.mainloop()
