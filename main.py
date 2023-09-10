import customtkinter as ti
from brain import *
from brain import agents_list
import pyautogui as pg
agents = agents_list("agents.json") # Get the names of the agents   

def root():
    print("building...")
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")
    
    root = ti.CTk()
    root.geometry("450x350")
    root.title("Valorant Instalocker")

    frame = ti.CTkFrame(root)
    frame.grid(row=1, column=1, padx=20, pady=20)

    frame2 = ti.CTkFrame(root)
    frame2.grid(row=1, column=2, padx=20, pady=20)

    label = ti.CTkLabel(frame, text="Start Key:")
    label.grid(row=1, column=1, padx=20, pady=1)

    entry1 = ti.CTkEntry(frame, placeholder_text=get_value("start_key"))
    entry1.grid(row=2, column=1, padx=20, pady=12)

    label = ti.CTkLabel(frame, text="End Key:")
    label.grid(row=3, column=1, padx=20, pady=1)

    entry2 = ti.CTkEntry(frame, placeholder_text=get_value("end_key"))
    entry2.grid(row=4, column=1, padx=20, pady=12)

    drop = ti.CTkOptionMenu(frame , values=agents)
    drop.grid(row=5, column=1, padx=20, pady=12)

    button = ti.CTkButton(frame, text="add agent", command=lambda: add_agents_frame())
    button.grid(row=6, column=1, padx=25, pady=20)
    
    label2 = ti.CTkLabel(frame2, text="If you already set an ")
    label2.grid(row=3, column=1, padx=25, pady=10)

    checkbox = ti.CTkCheckBox(frame2, text="Remember Keys")
    checkbox.grid(row=4, column=1, padx=25, pady=10)

    button = ti.CTkButton(frame2, text="Start", command=lambda: start(entry1.get(), entry2.get(), checkbox.get(), drop.get()))
    button.grid(row=5, column=1, padx=25, pady=7)

    

    

    label = ti.CTkLabel(frame2, text="made by Willi")
    label.grid(row=8, column=1, padx=25, pady=10)

    root.mainloop()

def add_agents_frame():
    print("building...")
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")

    root = ti.CTk()
    root.geometry("400x350")
    root.title("Add Agents")

    frame = ti.CTkFrame(root)
    frame.grid(row=1, column=1, padx=20, pady=20)

    entry3 = ti.CTkEntry(frame, placeholder_text="Enter Agentname")
    entry3.grid(row=1, column=1, padx=25, pady=10)
    
    button = ti.CTkButton(frame, text="add agent", command=lambda: add_agent(entry3.get()))
    button.grid(row=2, column=1, padx=25, pady=7)

    button3 = ti.CTkButton(frame, fg_color="red", text="Delete Agent", command=lambda: remove_agent("agents.json"))
    button3.grid(row=4, column=1, padx=25, pady=7)

    button3 = ti.CTkButton(frame, fg_color="green", text="Button", command=lambda: add_agent("Button"))
    button3.grid(row=3, column=1, padx=25, pady=7)
    
    root.mainloop()

if __name__ == "__main__":
    root()