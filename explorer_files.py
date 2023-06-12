from tkinter import *
   
from tkinter import filedialog 

#Select path
def browseFiles(): 
    filename = filedialog.askdirectory(
        initialdir = "/", 
        title = "Select a File", 
    ) 
    print(filename)
    return filename