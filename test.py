import customtkinter as ti
from brain import *
from time import sleep
import threading
from selfupdate import update
from PIL import Image, ImageTk

# The path of the json files
agents_json = resource_path(".vlocker\\agents.json")
settings_json = resource_path(".vlocker\\settings.json")

icon = resource_path(".vlocker\\icon.ico")

# Get the names of the agents 
agents = agents_list(agents_json) 

# Hippity hoppity your picture is now my property
background_image = resource_path(".vlocker\\background.jpg") 

# Thanks Google
# PhotoImage = ImageTk.PhotoImage(Image.open(resource_path(".vlocker\\delete.png")),width=28,height=28)
def root():
    print("root")
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")
    
    root = ti.CTk()
    root.geometry("450x330")
    root.title("Valorant Instalocker")
    root.iconbitmap(icon)

    asdf = ti.CTkImage(Image.open(background_image), size=(450, 330))
    background_label = ti.CTkLabel(root, text=None, image=asdf)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    scrollframe = ti.CTkScrollableFrame(root, width=400)
    scrollframe.grid(padx=20, pady=20)

    current_row = 2


    label = ti.CTkLabel(scrollframe, text="Button")
    label.grid(row=1, column=1, padx=25, pady=10)
    
    if get_value("Button", settings_json) != any:
        button = ti.CTkButton(scrollframe, fg_color="blue", compound=ti.LEFT, text="Update", command=lambda: update_value("Button",settings_json), width=28, height=28)
        button.grid(row=1, column=2, padx=10, pady=10)
    else:
        print("not set")
        
        
    for agent in agents:
        label = ti.CTkLabel(scrollframe, text=agent)
        label.grid(row=current_row, column=1, padx=25, pady=10)

        # Removes the Agent from the list
        button = ti.CTkButton(scrollframe, fg_color="red", compound=ti.LEFT, text="❌", command=lambda: remove_value(agents_json, agent), width=28, height=28)
        button.grid(row=current_row, column=3, padx=10, pady=10)

        # Updates the Agent in the list
        button = ti.CTkButton(scrollframe, fg_color="blue", compound=ti.LEFT, text="Update", command=lambda: update_value(agents_json, agent), width=28, height=28)
        button.grid(row=current_row, column=2, padx=10, pady=10)

        current_row += 1

    root.mainloop()

    
    

if __name__ == "__main__":
    root()
    