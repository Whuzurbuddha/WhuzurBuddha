import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import subprocess


def drawing_map():
    sql_command = "select longitude, latitude from germany"
    result = data_result(sql_command)
    lon = []
    lat = []
    for row in result:
        lon.append(row[0])
        lat.append(row[1])

    xLabel = "longitude"
    yLabel = "latitude"

    return lon, lat, xLabel, yLabel


def return_back():
    window.destroy()
    subprocess.run(["python3", "main.py"])


def data_result(sql_command):
    con = sqlite3.connect(PATH TO DATABASE)
    cursor = con.cursor()
    cursor.execute(sql_command)
    result = cursor.fetchall()

    return result


def distance(entry):
    input_value = entry.get()
    split = input_value.split(" ")
    if len(split) < 2:
        print("Enter start and end point.")
        return

    start = split[0]
    end = split[1]

    start_request = "SELECT latitude, longitude FROM germany WHERE place_name = '" + start + "'"
    start_result = data_result(start_request)
    if start_result:
        start = start_result[0][:2]

    end_request = "SELECT latitude, longitude FROM germany WHERE place_name = '" + end + "'"
    end_result = data_result(end_request)
    if end_result:
        end = end_result[0][:2]

    xLabel = "longitude"
    yLabel = "latitude"
    print("Start: " + str(start))
    print("End: " + str(end))
    return start, end


def load_map():

    fig.clear()

    map_data = drawing_map()
    lon = map_data[0]
    lat = map_data[1]

    ax = fig.add_subplot(111)
    ax.plot(lon, lat, color='g', marker='o', linestyle='None', markersize=15)
    canvas.draw()


def update_plot():
    fig.clear()

    map_data = drawing_map()
    lat = map_data[0]
    lon = map_data[1]

    distances = distance(input_entry)
    ax = fig.add_subplot(111)


    start = distances[0]
    end = distances[1]

    ax.plot(lat, lon, color='g', marker='o', linestyle='None', markersize=15)
    ax.plot(start[1], start[0], color='r', marker='o', linestyle='None', markersize=15)
    ax.plot(end[1], end[0], color='r', marker='o', linestyle='None', markersize=15)

    canvas.draw()


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Density")
    window.geometry("820x1000")
    window.resizable(False, False)

    fig = Figure(figsize=(8, 9), dpi=100)
    fig.set_facecolor('darkgray')
    ax = fig.add_subplot(111)

    load_button = tk.Button(window, text="Load map", command=load_map)
    load_button.grid(row=3, column=2, padx=2, pady=5, sticky=tk.EW)

    save_button = tk.Button(window, text="calculate", command=update_plot)
    save_button.grid(row=3, column=1, padx=2, pady=5, sticky=tk.EW)

    input_frame = tk.Frame(window)
    input_frame.grid(row=2, column=0, columnspan=4, pady=5, sticky=tk.EW)

    input_label = tk.Label(input_frame, text="Enter start and end point: ")
    input_label.pack(side=tk.LEFT, padx=10)

    input_entry = tk.Entry(input_frame)
    input_entry.pack(side=tk.LEFT)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky=tk.NSEW)

    window.protocol("WM_DELETE_WINDOW", return_back)

    window.mainloop()
