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
        self.title("distance calculator")
        self.geometry("820x1000")
        self.set_background_image("img/background.png")

        self.fig = Figure(figsize=(6, 8), dpi=100)
        self.fig.set_facecolor('darkgray')
        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=100, pady=55, sticky="nw")

        input_frame = tk.Frame(self)
        input_frame.grid(row=0, column=0, pady=50, sticky="s")

        input_label = tk.Label(input_frame, text="Enter start and end point: ")
        input_label.grid(row=0, column=0, padx=30, pady=5)

        self.input_entry = tk.Entry(input_frame)
        self.input_entry.grid(row=0, column=0, columnspan=15, padx=200, pady=10, sticky="s")

        self.load_button = tk.Button(self, text="clean map", command=self.load_map)
        self.load_button.grid(row=0, column=0, padx=400, pady=10, sticky="ws")

        self.save_button = tk.Button(self, text="calculate", command=self.update_plot)
        self.save_button.grid(row=0, column=0, padx=270, pady=10, sticky="ws")

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

        img = Image.open("img/th-1.png")
        self.ax.imshow(img, extent=[min(lon), max(lon), min(lat), max(lat)], aspect='auto')

        self.canvas.draw()

    def return_back(self):
        self.destroy()
        subprocess.run(["python3", "main.py"])

    def update_plot(self):
        self.ax.clear() 

        map_data = self.drawing_map()
        lat = map_data[0]
        lon = map_data[1]

        distances = self.distance(self.input_entry)
        start = distances[0]
        end = distances[1]
        s_name = distances[2]
        e_name = distances[3]
        print(f"{s_name}: {start[0]}:{start[1]}")
        print(e_name)

        dist = self.haversine(start[0], start[1], end[0], end[1])
        km = int(dist)

        img = Image.open("img/th-1.png")
        self.ax.imshow(img, extent=[min(lat), max(lat), min(lon), max(lon)], aspect='auto')

        self.ax.plot(start[1], start[0], color='red', marker='o', markersize=10)
        self.ax.plot(end[1], end[0], color='yellow', marker='o', linestyle='dotted', markersize=10)

        self.ax.set_title(f"Distance is {km}km ")
        self.ax.annotate(f"{s_name}", xy=(start[1], start[0]), xytext=(-20, 10),
                         textcoords="offset points", ha='center', fontsize=8,
                         bbox=dict(boxstyle="round", fc="w", ec="gray"))
        self.ax.annotate(f"{e_name}", xy=(end[1], end[0]), xytext=(-20, 10),
                         textcoords="offset points", ha='center', fontsize=8,
                         bbox=dict(boxstyle="round", fc="w", ec="gray"))

        self.canvas.draw()

    def distance(self, entry):
        input_value = entry.get()
        split = input_value.split(" ")
        if len(split) < 2:
            print("Enter start and end point.")
            return

        start = split[0]
        end = split[1]

        start_request = "SELECT latitude, longitude, place_name FROM germany WHERE place_name = '" + start + "'"
        start_result = self.data_result(start_request)
        if start_result:
            start = start_result[0][:2]
            start_name = start_result[0][2]

        end_request = "SELECT latitude, longitude, place_name FROM germany WHERE place_name = '" + end + "'"
        end_result = self.data_result(end_request)
        if end_result:
            end = end_result[0][:2]
            end_name = end_result[0][2]

        xLabel = "longitude"
        yLabel = "latitude"

        return start, end, start_name, end_name

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        radius = 6371

        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = radius * c
        return distance


if __name__ == '__main__':
    app = App()
    app.mainloop()
