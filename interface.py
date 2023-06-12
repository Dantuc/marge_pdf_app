

import tkinter as tk
from explorer_files import browseFiles
from merge_pdf import merge_pdf
import os


def save_name_and_merge(file_name: tk.StringVar, marge_button: tk.Button):

    final_name = file_name.get()

    if final_name == "":
        warning = warning_label("#A0522D")
        return warning
    
    warning = warning_label(background_color)
    path = browseFiles()
    output_path = path +"/" + final_name + ".pdf"
    merge_pdf(path, output_path)
    return

#config button standard
def button_config(name):
    button_config = tk.Button(
        root, 
        text= name, 
        padx=(10),
        background= "#D2691E",
        relief = "flat"
        )
    return button_config

#config label standard
def label_config(title):
    label_config = tk.Label(
    root,
    text= title,
    background= background_color, 
    font=("Helvetica", 12),
    )
    return label_config

#warning label:
def warning_label(fg):
    warning = tk.Label(
        root,
        text= "Digite um nome válido!!",
        background= background_color, 
        font=("Helvetica", 7),
        fg=fg
        )
    warning.grid(row= 3, column= 1)
    

root = tk.Tk()

title = "PDF Merger"
background_color = "#F5DEB3"

# Title config
main_tittle = tk.Label(
    root,
    text= title,
    background= background_color, 
    font=("Helvetica", 12, "bold"),
)
main_tittle.grid(row=0, column=0, columnspan=3, pady=(0,20))

# Text config
file_label = label_config("Nome do arquivo: ")
file_label.grid(row=2, column=0)

#Entry name config
file_name = tk.StringVar()
validate_entry = tk.Entry(
    root,
    bd=5,
    relief = "flat",
    textvariable= file_name
)
validate_entry.grid(row= 2, column= 1)

#merge button config
merge_button = button_config("Merge")
merge_button.grid(row= 2, column= 2)
merge_button.config(command= lambda: save_name_and_merge(file_name, merge_button))



root.title(title)
root.config(background= background_color, padx=20, pady= 20)
root.mainloop()
