# Importing Packages (TKinter, OS, filedialog, )
import os
import tkinter as tk
from tkinter import filedialog


# App Coding (Scripts)
root = tk.Tk()
apps = []

# Icon
root.iconbitmap("favicon.ico")





root.title('Soka')


def add_app():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Executable", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def run_apps():
    for app in apps:
        os.startfile(app)

def quit():
    root.quit()
# Menu Bar
menu_bar = tk.Menu(root)
file_bar = tk.Menu(menu_bar, tearoff=0)
file_bar.add_command(label='Add', command=add_app)
file_bar.add_command(label='Close Soka', command=root.quit)
menu_bar.add_cascade(label='File', menu=file_bar)
root.config(menu=menu_bar)
run_bar = tk.Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run_apps)
menu_bar.add_cascade(label='Run', menu=run_bar)
root.config(menu=menu_bar)
# Canvas, Frame, Buttons
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=add_app)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263D42", command=run_apps)
runApps.pack()

quit_soka= tk.Button(root, text="Quit Soka", padx=10,pady=5, fg="white", bg="#263D42", command=quit)
quit_soka.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# Running
root.mainloop()