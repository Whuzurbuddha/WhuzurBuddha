import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import subprocess


def return_back():
    window.destroy()
    subprocess.run(["python3", "main.py"])


def data_result(sql_command):
    con = sqlite3.connect(PATH TO DATABASE)
    cursor = con.cursor()
    cursor.execute(sql_command)
    result = cursor.fetchall()

    return result


def states():
    states = "SELECT DISTINCT admin_name_1 FROM germany"
    states_result = data_result(states)

    state_coordinates = {}

    for row in states_result:
        state_name = row[0]
        sql_command = "SELECT latitude, longitude FROM germany WHERE admin_name_1 = '" + state_name + "' ORDER BY latitude"
        result = data_result(sql_command)

        coordinates = []
        for coordinate_row in result:
            coordinates.append(coordinate_row)

        state_coordinates[state_name] = coordinates

    return state_coordinates


def drawing_map():
    sql_command = "select latitude, longitude from germany order by latitude"
    result = data_result(sql_command)
    lat = []
    lon = []
    for row in result:
        lat.append(row[0])
        lon.append(row[1])

    xLabel = "longitude"
    yLabel = "latitude"

    return lat, lon, xLabel, yLabel


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Density")
    window.geometry("800x1000")

    fig = Figure(figsize=(5, 4), dpi=100)
    fig.set_facecolor('darkgray')
    ax = fig.add_subplot(111)

    map_data = drawing_map()
    lat = map_data[0]
    lon = map_data[1]
    xLabel = map_data[2]
    yLabel = map_data[3]
    state_coordinates = states()
    for state, coordinates in state_coordinates.items():
        lat = [coord[0] for coord in coordinates]
        lon = [coord[1] for coord in coordinates]
        ax.plot(lon, lat, marker='.', linestyle='None', markersize=20)

    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    window.protocol("WM_DELETE_WINDOW", return_back)

    window.mainloop()
