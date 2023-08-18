import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()


def addApp():
    filename = filedialog.askopenfilename(intia ldir="/", title="select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))


canvas = tk.Canvas(root, height=700, bg="#263D42", width=700)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open file", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263D42")
runApps.pack()

root.mainloop()
