import sqlite3
import subprocess
import math
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("simple map")
        self.geometry("820x1000")
        self.resizable(False, False)
        self.set_background_image("img/background.png")

        self.fig = Figure(figsize=(6, 8), dpi=100)
        self.fig.set_facecolor('darkgray')
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=110, pady=100, sticky="nw")

        self.load_map()

        self.protocol("WM_DELETE_WINDOW", self.return_back)

    def set_background_image(self, image_path):
        image = Image.open(image_path)
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.grid(row=0, column=0, padx=0, sticky="nw")

    @staticmethod
    def data_result(sql_command):
        con = sqlite3.connect(PATH TO DATABASE)
        cursor = con.cursor()
        cursor.execute(sql_command)
        result = cursor.fetchall()

        return result

    def drawing_map(self):
        sql_command = "select longitude, latitude from germany"
        result = self.data_result(sql_command)
        lon = []
        lat = []
        for row in result:
            lon.append(row[0])
            lat.append(row[1])

        xLabel = "longitude"
        yLabel = "latitude"

        return lon, lat, xLabel, yLabel

    def load_map(self):
        self.ax.clear()

        map_data = self.drawing_map()
        lon = map_data[0]
        lat = map_data[1]

        self.ax.plot(lon, lat, color='g', marker='o', linestyle='None', markersize=2)

        self.canvas.draw()

    def return_back(self):
        self.destroy()
        subprocess.run(["python3", "main.py"])


if __name__ == '__main__':
    app = App()
    app.mainloop()
