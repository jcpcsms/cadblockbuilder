import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Select Option")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60,fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="CAD BlockBuilder Beta")
label.pack(pady=12, padx=12)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="BlockBuilder")
entry1.pack(pady=12, padx=12)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Image Scan")
entry2.pack(pady=12, padx=12)

root.mainloop()
