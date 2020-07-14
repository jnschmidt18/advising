import tkinter as tk
from tkinter import filedialog as fd

root=tk.Tk()

def getfile():      #gets file from OS dialog
    root.filename=fd.askopenfilename(initialdir = "/Desktop",title = "Select File",filetypes = (("html files","*.html"),("all files","*.*")))
    return(root.filename)
    tk.mainloop()

def writeToWindow(text):
    scroll=tk.Scrollbar(root)
    textspace=tk.Text(root, height=40, width=100)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    textspace.pack(side=tk.LEFT, fill=tk.Y)
    scroll.config(command=textspace.yview)
    textspace.config(yscrollcommand=scroll.set)
    textspace.insert(tk.END, text)
    tk.mainloop()
