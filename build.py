import customtkinter as ti
import main
import time as tm
from agent_manager import *
import settings

agents = agents_list("btn_location.json")

def root(a="run"):
    print("building...")
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")
    
    root = ti.CTk()
    root.geometry("500x350")
    frame = ti.CTkFrame(root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    entry1 = ti.CTkEntry(frame, placeholder_text="Enter Start Key")
    entry1.pack(pady=10, padx=10)

    entry2 = ti.CTkEntry(frame, placeholder_text="Enter Stop Key")
    entry2.pack(pady=10, padx=10)

    checkbox = ti.CTkCheckBox(frame, text="Remember")
    checkbox.pack(pady=12, padx=10)

    # initial menu text
    #clicked.set(default_agent)
    drop = ti.CTkOptionMenu(frame , values=agents)
    drop.pack(pady=10, padx=10)

    button = ti.CTkButton(root, text="Start", command=lambda: main.start(entry1.get(), entry2.get(), checkbox.get()))
    button.pack(pady=10, padx=10)


    root.mainloop()

def agent_manager():
    tm.sleep(1)