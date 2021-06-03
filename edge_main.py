import tkinter as tk
import tkinter.filedialog as fdialog
import edge
import os

gui = tk.Tk()
gui.title("Simple Signal Program")
gui.geometry("480x220")


def folderselect(desc):
    currdir = os.getcwd()
    tempdir = fdialog.askopenfilename(parent=gui, initialdir=currdir, title='Please select a directory')
    if desc == 5:
        img_edge(tempdir)


def img_edge(tempdir):
    edgetk = tk.Toplevel()
    edgetk.title("Edge Detection")
    edgetk.geometry("320x160")
    execnow = tk.Button(edgetk, text="Basic Edge Detection", command=lambda: EdgeD(tempdir, 1))
    execnow.grid(row=0, column=0)
    execnow = tk.Button(edgetk, text="Sobel", command=lambda: EdgeD(tempdir, 2))
    execnow.grid(row=1, column=0)


def EdgeD(tempdir, decision):
    ed = edge.Edgetrans(tempdir)
    ed.readimg(decision)

edgy = tk.Button(gui, text="Edge Detection", command=lambda: folderselect(5))
edgy.grid(row=4, column=1)
gui.mainloop()
