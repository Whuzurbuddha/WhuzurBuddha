import subprocess
import tkinter as tk
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("820x1000")
        self.resizable(False, False)
        self.title('PyMap')
        self.config(background='darkgray')
        self.programs = ('Map', 'Density', 'States', "Calculating distance")
        self.option_var = tk.StringVar(self)
        self.set_background_image("img/background.png")
        self.create_widgets()

    def create_widgets(self):
        paddings = {'padx': 10, 'pady': 10}

        label = tk.Label(self, text='Select program to run')
        label.grid(column=1, row=0, sticky=tk.NW)

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            self.programs[0],
            *self.programs,
            command=self.option_changed)

        option_menu.grid(column=0, row=0, sticky=tk.NW)

    def set_background_image(self, image_path):
        image = Image.open(image_path)
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.grid(column=0, row=0, sticky=tk.NSEW)

    def option_changed(self, *args):
        program_list = ["Map", "Density", "States", "Calculating distance"]
        executable_programs = ["map.py", "density.py", "states.py", "calc_distance.py"]
        choice = self.option_var.get()
        for i in range(len(program_list)):
            if choice == program_list[i]:
                self.destroy()
                subprocess.run(["python3", executable_programs[i]])


if __name__ == '__main__':
    app = App()
    app.mainloop()
