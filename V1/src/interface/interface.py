import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def gui():
    #Get data
    def get_clicked():
        project_name = name.get()
        if ' ' in project_name:
            project_name = project_name.replace(' ', '_')
        if '-' in project_name:
            project_name = project_name.replace('-', '_')
        if '.' in project_name:
            project_name = project_name.replace('.', '_')
        if ':' in project_name:
            project_name = project_name.replace(':', '_')
        if ';' in project_name:
            project_name = project_name.replace(';', '_')
        if ',' in project_name:
            project_name = project_name.replace(',', '_')
        if '!' in project_name:
            project_name = project_name.replace('!', '_')
        if '?' in project_name:
            project_name = project_name.replace('?', '_')
        if '"' in project_name:
            project_name = project_name.replace('"', '_')
        
        root.quit()
        
        return [path.get(),project_name]

    # root window
    root = tk.Tk()
    root.geometry("300x150")
    root.resizable(False, False)
    root.title('Angular Projects Builder')

    # store name address and path
    name = tk.StringVar()
    path = tk.StringVar()


    # Sign in frame
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=True)

    # name
    name_label = ttk.Label(signin, text="Enter the name of your project:")
    name_label.pack(fill='x', expand=True)

    name_entry = ttk.Entry(signin, textvariable=name)
    name_entry.pack(fill='x', expand=True)
    name_entry.focus()

    # path
    path_label = ttk.Label(signin, text="Enter here the pwd, Ex. /Users/user/Desktop/env ...")
    path_label.pack(fill='x', expand=True)

    path_entry = ttk.Entry(signin, textvariable=path)
    path_entry.pack(fill='x', expand=True)

    # login button
    get_button = ttk.Button(signin, text="Begin process...", command=get_clicked)
    get_button.pack(fill='x', expand=True, pady=10)

    root.mainloop()
    return get_clicked()

