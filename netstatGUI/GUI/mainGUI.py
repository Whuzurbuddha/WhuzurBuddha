import tkinter as tk
import subprocess



def center_text(widget, new_text):
    widget.configure(state='normal', fg="red")
    widget.tag_configure("center", justify='center')
    widget.insert(tk.END, '\n\n\n')
    widget.insert("1.0", '\n'
                         '\n'
                         '    ++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++' '\n'
                         ' ''\n'
                         ' ''\n'
                         '     ::::    :::    ::::::::::  :::::::::::   ::::::::   :::::::::::      :::    :::::::::::                 ::::::::   :::    :::  ::::::::::: ' '\n'
                         '  :+:+:   :+:    :+:             :+:      :+:    :+:      :+:        :+: :+:      :+:         *          :+:    :+:   :+:    :+:      :+: ' '\n'
                         '  :+:+:+  +:+    +:+             +:+      +:+             +:+       +:+   +:+     +:+         #          +:+          +:+    +:+      +:+ ' '\n'
                         '  +#+ +:+ +#+    +#++:++#        +#+      +#++:++#++      +#+      +#++:++#++:    +#+    ++:++#++:++     :#:          +#+    +:+      +#+ ' '\n'
                         '  +#+  +#+#+#    +#+             +#+             +#+      +#+      +#+     +#+    +#+         #          +#+   +#+#   +#+    +#+      +#+ ' '\n'
                         ' #+#   #+#+#    #+#             #+#      #+#    #+#      #+#      #+#     #+#    #+#         *          #+#    #+#   #+#    #+#      #+# ' '\n'
                         '     ###    ####    ##########      ###       ########       ###      ###     ###    ###                    ########     ########    ########### ' '\n'
                         ' ''\n'
                         ' ''\n'
                         '    ++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++#++:++++:++' '\n'
                         '©'" written by A.Paeplow", "center")
    widget.insert(tk.END, new_text)
    widget.configure(state='disabled')
    widget.insert(tk.END, "\n")


def start():
    center_text(text, "\n")
    text.insert(tk.END, "\n\n\n\n")


def dispContent(file: str):
    clear_text()
    text.insert(tk.END, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    try:
        with open(f"/home/alexander/CLionProjects/NETstetGUI/output/{file}", "r") as file:
            output = file.read()
            center_text(text, output)
    except FileNotFoundError:
        text.insert(tk.END, "Output file not found.")


def clear_text():
    text.configure(state='normal')
    text.delete("1.0", tk.END)
    text.configure(state='disabled')

def delete_content():
    content_files = ["acs.txt", "acws.txt", "interout.txt", "outrouting.txt" ]
    for i in range(0, 4):
        try:
            with open(f"/home/alexander/CLionProjects/NETstetGUI/output/{content_files[i]}", "w") as file:
                file.write(" ")
        except FileNotFoundError:
            text.insert(tk.END, "Output file not found.")


def execute_main():
    try:
        subprocess.run(["/home/alexander/CLionProjects/NETstetGUI/src/run"])
    except FileNotFoundError:
        text.insert(tk.END, "Error: main.cpp not found.")
        return


root = tk.Tk()
root.title("NETSTAT-GUI")
root.geometry("1400x900")

text = tk.Text(root, fg="yellow", bg="black")
text.pack(fill=tk.BOTH, expand=True)

button = tk.Button(root, text="Routing table", command=lambda: [delete_content, execute_main(), dispContent("outrouting.txt")])
button.pack(side=tk.LEFT)

button = tk.Button(root, text="Interfaces", command=lambda:  [delete_content, execute_main(), dispContent("interout.txt")])
button.pack(side=tk.LEFT)

button = tk.Button(root, text="Connections (just Server)",
                   command=lambda: [delete_content, execute_main(), dispContent("acws.txt")])
button.pack(side=tk.LEFT)

button = tk.Button(root, text="Connections (without Server)",
                   command=lambda:  [delete_content, execute_main(), dispContent("acs.txt")])
button.pack(side=tk.LEFT)

start()
root.mainloop()
delete_content()
