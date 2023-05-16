import tkinter as tk

def dispRouting():
    text.delete(1.0, tk.END)  # Vorherigen Text löschen
    try:
        with open("/home/alexander/CLionProjects/NETstetGUI/output/outrouting.txt", "r") as file:
            output = file.read()
            text.insert(tk.END, output)
    except FileNotFoundError:
        text.insert(tk.END, "Output file not found.")

def dispInterfaces():
    text.delete(1.0, tk.END)  # Vorherigen Text löschen
    try:
        with open("/home/alexander/CLionProjects/NETstetGUI/output/interout.txt", "r") as file:
            output = file.read()
            text.insert(tk.END, output)
    except FileNotFoundError:
        text.insert(tk.END, "Output file not found.")

def dispConnectServer():
    text.delete(1.0, tk.END)  # Vorherigen Text löschen
    try:
        with open("/home/alexander/CLionProjects/NETstetGUI/output/acs.txt", "r") as file:
            output = file.read()
            text.insert(tk.END, output)
    except FileNotFoundError:
        text.insert(tk.END, "Output file not found.")

def dispConnectWServer():
    text.delete(1.0, tk.END)
    try:
        with open("/home/alexander/CLionProjects/NETstetGUI/output/acws.txt", "r") as file:
            output = file.read()
            text.insert(tk.END, output)
    except FileNotFoundError:
        text.insert(tk.END, "Output file not found.")


root = tk.Tk()
text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

button = tk.Button(root, text="Routing table", command=dispRouting)
button.pack(side=tk.LEFT)

button = tk.Button(root, text="Interfaces", command=dispInterfaces)
button.pack(side=tk.LEFT)

button = tk.Button(root, text="Connections (with Server)", command=dispConnectServer)
button.pack(side=tk.LEFT)

button = tk.Button(root, text="Connections (without Server)", command=dispConnectWServer)
button.pack(side=tk.LEFT)

root.mainloop()
