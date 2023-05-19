def projectName():
    project_name = input("Enter the name of your project: ")
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
    return project_name
    