# Thanks ChatGPT
import customtkinter as ti
from brain import *
from time import sleep
import threading
from selfupdate import update
from PIL import Image, ImageTk

class ValorantInstalockerApp:
    def __init__(self):
        self.agents_json = resource_path(".vlocker\\agents.json")
        self.settings_json = resource_path(".vlocker\\settings.json")
        self.icon = resource_path(".vlocker\\icon.ico")

        ti.set_appearance_mode("dark")
        ti.set_default_color_theme("dark-blue")

        self.root = ti.CTk()
        self.root.geometry("450x330")
        self.root.title("Valorant Instalocker")
        self.root.iconbitmap(self.icon)

        self.background_image = resource_path(".vlocker\\background.jpg")
        self.asdf = ti.CTkImage(Image.open(self.background_image), size=(450, 330))

        self.background_label = ti.CTkLabel(self.root, text=None, image=self.asdf)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.scrollframe = ti.CTkScrollableFrame(self.root, width=400)
        self.scrollframe.grid(padx=20, pady=20)

    def create_agent_buttons(self):
        current_row = 2

        label = ti.CTkLabel(self.scrollframe, text="Button")
        label.grid(row=1, column=1, padx=25, pady=10)

        if get_value("Button", self.settings_json) != any:
            button_text = "edit"
            fg_color = "blue"
        else:
            button_text = "set"
            fg_color = "red"

        button = ti.CTkButton(self.scrollframe, fg_color=fg_color, compound=ti.LEFT, text=button_text,
                              command=lambda: update_value("Button", self.settings_json), width=28, height=28)
        button.grid(row=1, column=2, padx=10, pady=10)

        for agent in agents_list(self.agents_json):
            label = ti.CTkLabel(self.scrollframe, text=agent)
            label.grid(row=current_row, column=1, padx=25, pady=10)

            def remove_agent(a=agent):
                remove_value(a, self.agents_json)
                self.refresh_scrollframe()
                self.root.update_idletasks()

            button_remove = ti.CTkButton(self.scrollframe, fg_color="red", command=remove_agent,
                                         compound=ti.LEFT, text="❌", width=28, height=28)
            button_remove.grid(row=current_row, column=3, padx=10, pady=10)

            def update_agent(a=agent):
                update_value(self.agents_json, a)

            button_update = ti.CTkButton(self.scrollframe, fg_color="blue", compound=ti.LEFT, text="Update",
                                         command=update_agent, width=28, height=28)
            button_update.grid(row=current_row, column=2, padx=10, pady=10)

            current_row += 1

    def refresh_scrollframe(self):
        for widget in self.scrollframe.winfo_children():
            widget.destroy()

        self.create_agent_buttons()

    def main(self):
        self.create_agent_buttons()
        self.root.mainloop()

if __name__ == "__main__":
    app = ValorantInstalockerApp()
    app.main()