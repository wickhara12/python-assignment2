"""Task 14 was done by LeRoi and task 7 was created by Rebecca"""
import pickle
import os
from tkinter import *
from tkinter import filedialog


root = Tk()
try:
    name_of_file = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("All files", "*.*")))
    with open(name_of_file) as file:
        file_data = file.read()
        root.destroy()
        print("\nfile loaded...\n")

except FileNotFoundError:
    root.destroy()
    print("Error, no file inserted")


@staticmethod
def choose_directory():
    root = Tk()
    try:
        dir_name = filedialog.askdirectory()
        root.destroy()
        return dir_name
    except FileNotFoundError:
        root.destroy()

with open("data.pickle", "wb") as f:
    pickle.dump(file_data, f)

with open("data.pickle", "rb") as f:
    data = pickle.load(f)
print(data)


