import tkinter as tk
from explorer_files import browseFiles


def save_name(file_name: tk.StringVar, marge_button: tk.Button):
    print(file_name.get())
    return file_name.get()

def button_config(name):
    button_config = tk.Button(
        root, 
        text= name, 
        padx=(10),
        background= "#D2691E",
        relief = "flat"
        )
    return button_config

def label_config(title):
    label_config = tk.Label(
    root,
    text= title,
    background= background_color, 
    font=("Helvetica", 12),
    )
    return label_config

root = tk.Tk()

title = "PDF Marger"
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

# Text config
explorer_label = label_config("Escolha uma pasta: ")
explorer_label.grid(row=1, column=0)

#Entry name config
file_name = tk.StringVar()
validate_entry = tk.Entry(
    root,
    bd=5,
    relief = "flat",
    textvariable= file_name
)
validate_entry.grid(row= 2, column= 1)

#explorer button config
explorer_button = button_config("Select Path")
explorer_button.grid(row= 1, column= 1)
explorer_button.config(command= browseFiles)

#marge button config
marge_button = button_config("Marge")
marge_button.grid(row= 2, column= 2)
marge_button.config(command= lambda: save_name(file_name, marge_button))



root.title(title)
root.config(background= background_color, padx=20, pady= 20)
root.mainloop()
