from tkinter import *
   
from tkinter import filedialog 

def browseFiles(): 
    filename = filedialog.askdirectory(
        initialdir = "/", 
        title = "Select a File", 
    ) 
    print(filename)
    return browseFiles