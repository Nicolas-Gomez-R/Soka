# Importando paquetes TKinter, os ,filedialog, Pillow (Almohada, para el icono)
import os
import tkinter as tk
from tkinter import filedialog

from setuptools import Command


# Codigo Base
root = tk.Tk()
apps = []

# Icono
root.iconbitmap("favicon.ico")




root.title('Soka')


# Comandos
def add_app():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Seleccionar Archivo",
                                          filetypes=(("Ejecutable", "*.exe"), ("all files", "*.*")))
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
# Canvas y Frame
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Botones
openFile = tk.Button(root, text="Abrir archivo", padx=10,
                     pady=5, fg="white", bg="#263D42", command=add_app)
openFile.pack()

runApps = tk.Button(root, text="Ejecutar Aplicaciones", padx=10,
                    pady=5, fg="white", bg="#263D42", command=run_apps)
runApps.pack()

quit_soka= tk.Button(root, text="Cerrar Soka", padx=10,pady=5, fg="white", bg="#263D42", command=quit)
quit_soka.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# Running
root.mainloop()

