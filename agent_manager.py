import customtkinter as ti
from brain import *
from PIL import Image
import threading

agents_json = resource_path(".vlocker\\agents.json")
settings_json = resource_path(".vlocker\\settings.json")
icon = resource_path(".vlocker\\icon.ico")

def create_agent_buttons(scrollframe, agents_json, settings_json):
    current_row = 2

    label = ti.CTkLabel(scrollframe, text="Button")
    label.grid(row=1, column=1, padx=25, pady=10)

    if get_value("Button", settings_json) != any:
        button_text = "edit"
        fg_color = "blue"
    else:
        button_text = "set"
        fg_color = "red"

    button = ti.CTkButton(scrollframe, fg_color=fg_color, compound=ti.LEFT, text=button_text,
            command=lambda: edit_item("Button", settings_json, scrollframe), width=28, height=28)

    button.grid(row=1, column=2, padx=10, pady=10)

    agents = agents_list(agents_json)

    for agent in agents:
        label = ti.CTkLabel(scrollframe, text=agent)
        label.grid(row=current_row, column=1, padx=25, pady=10)

        def remove_agent(a=agent):
            remove_item(a, agents_json)
            refresh_scrollframe(scrollframe, agents_json, settings_json)

        button_remove = ti.CTkButton(scrollframe, fg_color="red", command=remove_agent,
                                     compound=ti.LEFT, text="❌", width=28, height=28)
        button_remove.grid(row=current_row, column=3, padx=10, pady=10)

        button_update = ti.CTkButton(scrollframe, fg_color="blue", compound=ti.LEFT, text="Update", 
                command=lambda a=agent: edit_item(a, agents_json, scrollframe), width=28, height=28)
        button_update.grid(row=current_row, column=2, padx=10, pady=10)

        agent_pos = get_value(agent, agents_json)

        label_position = ti.CTkLabel(scrollframe, text=f"{agent_pos[0]}, {agent_pos[1]}")
        label_position.grid(row=current_row, column=4, padx=10, pady=10)

        current_row += 1

def refresh_scrollframe(scrollframe, agents_json, settings_json):
    for widget in scrollframe.winfo_children():
        widget.destroy()

    create_agent_buttons(scrollframe, agents_json, settings_json)

def agent_manager():
    

    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")

    root = ti.CTkToplevel()
    root.geometry("450x320")
    root.iconbitmap(icon)
    root.title("Manage Agents")
    root.resizable(False, False)
    root.attributes('-topmost', 1)

    background_image = resource_path(".vlocker\\background.jpg")
    asdf = ti.CTkImage(Image.open(background_image), size=(450, 330))

    background_label = ti.CTkLabel(root, text=None, image=asdf)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    scrollframe = ti.CTkScrollableFrame(root, width=400)
    scrollframe.grid(row=1, column=1, padx=20, pady=20)

    frame = ti.CTkFrame(root)
    frame.grid(row=2, column=1, padx=20, pady=20)

    entry = ti.CTkEntry(frame, placeholder_text="Enter Agentname")
    entry.grid(row=1, column=1, padx=25, pady=10)

    button = ti.CTkButton(frame, text="add agent", command=lambda: edit_item(entry.get(), agents_json, scrollframe))
    button.grid(row=1, column=2, padx=25, pady=7)

    create_agent_buttons(scrollframe, agents_json, settings_json)

    root.mainloop()

def edit_item(item, json_file_path, scrollframe):
    ti.set_appearance_mode("dark")
    ti.set_default_color_theme("dark-blue")

    root = ti.CTkToplevel()
    root.geometry("240x150")
    root.title("add/edit agent")
    root.iconbitmap(icon)
    root.resizable(False, False)
    root.attributes('-topmost', 2)

    def asdf(item, json_file_path):
        result = add_item(item, json_file_path)
        refresh_scrollframe(scrollframe, agents_json, settings_json)
        if result:
            root.destroy()


    frame = ti.CTkFrame(root)
    frame.grid(row=1, column=1, padx=20, pady=20)

    label = ti.CTkLabel(frame, text=f"hover over {item} and then \n press q.")
    label.grid(row=1, column=1, padx=25, pady=25)

    button = ti.CTkButton(frame, text="ok", command=lambda: root.attributes('-topmost', 0))
    button.grid(row=2, column=1, padx=25, pady=7)

    threading.Thread(target=asdf, args=(item, json_file_path)).start()
    
    root.mainloop()

if __name__ == "__main__":
    agent_manager()