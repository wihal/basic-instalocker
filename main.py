import customtkinter as ti
from brain import *

agents = agents_list("agents.json") # Get the names of the agents

def root():
    print("building...")
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")
    
    root = ti.CTk()
    root.geometry("500x350")
    root.title("Valorant Instalocker")

    frame = ti.CTkFrame(root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    frame2 = ti.CTkFrame(root)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)

    entry1 = ti.CTkEntry(frame, placeholder_text="Enter Start Key")
    entry1.grid(row=1, column=1, padx=20, pady=20)

    entry2 = ti.CTkEntry(frame, placeholder_text="Enter Stop Key")
    entry2.grid(row=1, column=2, padx=20, pady=20)

    # initial menu text
    #clicked.set(default_agent)
    drop = ti.CTkOptionMenu(frame2 , values=agents)
    drop.grid(row=4, column=1, padx=25, pady=7)

    checkbox = ti.CTkCheckBox(frame2, text="Remember")
    checkbox.grid(row=4, column=2, padx=25, pady=10)

    button = ti.CTkButton(frame2, text="Start", command=lambda: start(entry1.get(), entry2.get(), checkbox.get()))
    button.grid(row=5, column=2, padx=25, pady=7)

    label = ti.CTkLabel(frame2, text="made by Willi")
    label.grid(row=6, column=2, padx=25, pady=10)

    root.mainloop()

if __name__ == "__main__":
    root()