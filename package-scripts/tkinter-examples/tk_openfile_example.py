from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

print(root.filename)
