import tkinter as tk
import subprocess


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x60")
        self.title('Germany statics')
        self.config(background='darkgray')

        self.programs = ('Map', 'Density', 'States')

        self.option_var = tk.StringVar(self)

        self.create_widgets()

    def create_widgets(self):
       
        paddings = {'padx': 10, 'pady': 10}

        label = tk.Label(self, text='Select program to run: ')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            self.programs[0],
            *self.programs,
            command=self.option_changed)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

    def option_changed(self, *args):
        program_list = ["Map", "Density", "States"]
        executable_programs = ["map.py", "density.py", "states.py"]
        choice = self.option_var.get()
        for i in range(len(program_list)):
            if choice == program_list[i]:
                self.destroy()
                subprocess.run(["python3", executable_programs[i]])


if __name__ == '__main__':
    app = App()
    app.mainloop()
