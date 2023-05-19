import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

THEMES = [
    'cerulean',
    'cosmo',
    'cyborg',
    'darkly',
    'flatly',
    'journal',
    'litera',
    'lumen',
    'lux',
    'materia',
    'minty',
    'morph',
    'pulse',
    'quartz',
    'sandstone',
    'simplex',
    'sketchy',
    'slate',
    'solar',
    'spacelab',
    'superhero',
    'united',
    'vapor',
    'yeti',
    'zephyr'
]


def gui():
    # Get data
    def get_clicked():
        # Definir estilo bootswatch
        style = bootswatch.get().lower()
        theme = 'cosmo'
        if style in THEMES:
            theme = style
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

        return [path.get(), project_name, theme, backend.get().lower()]

    # root window
    root = tk.Tk()
    root.geometry("450x225")
    root.resizable(False, False)
    root.title('Angular Projects Builder')

    # store name address and path
    name = tk.StringVar()
    path = tk.StringVar()
    bootswatch = tk.StringVar()
    backend = tk.StringVar()

    # Sign in frame
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=True)

    # Nombre proyecto
    name_label = ttk.Label(signin, text="Ingresar nombre del proyecto:")
    name_label.pack(fill='x', expand=True)

    name_entry = ttk.Entry(signin, textvariable=name)
    name_entry.pack(fill='x', expand=True)
    name_entry.focus()

    # path
    path_label = ttk.Label(
        signin, text="Ingresar la ruta del proyecto, Ex. /Users/user/Desktop/env ...")
    path_label.pack(fill='x', expand=True)

    path_entry = ttk.Entry(signin, textvariable=path)
    path_entry.pack(fill='x', expand=True)

    # estilo bootswatch
    bootswatch_label = ttk.Label(
        signin, text="Ingresar el nombre del estilo a usar, ver el link https://bootswatch.com")
    bootswatch_label.pack(fill='x', expand=True)

    bootswatch_entry = ttk.Entry(signin, textvariable=bootswatch)
    bootswatch_entry.pack(fill='x', expand=True)

    # Se necesita crear el backend
    backend_label = ttk.Label(
        signin, text="Servicio backend, (Si o No) para crearlo.")
    backend_label.pack(fill='x', expand=True)

    backend_entry = ttk.Entry(signin, textvariable=backend)
    backend_entry.pack(fill='x', expand=True)

    # boton ingresar
    get_button = ttk.Button(
        signin, text="Begin process...", command=get_clicked)
    get_button.pack(fill='x', expand=True, pady=10)

    root.mainloop()
    return get_clicked()
