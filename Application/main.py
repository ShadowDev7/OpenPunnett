import customtkinter as ctk

def main():
    app = ctk.CTk()

    # theme and color options
    ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("dark-blue")
    # Buttons

    my_button = ctk.CTkButton(app, 
                              text="Click Me", 
                              command=lambda: label.configure(text=my_button.cget("text")),
                              height=40,
                              width=120,
                              font=("Arial", 14),
                              text_color="black",
                              fg_color="white",
                              hover_color="gray",
                              corner_radius=20,
                              bg_color="white"
                            )
    my_button.pack(pady=80)

    label = ctk.CTkLabel(app, text="")
    label.pack(pady=20)

    app.mainloop()


if __name__ == "__main__":
    main()