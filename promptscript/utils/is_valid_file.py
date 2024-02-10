import os

### Valid extensions for promptscript
# .../file.prompt
# OR
# .../file
###

def is_promptscript_file(file_path: str) -> bool:
    path_components = file_path.split('/')
    file_name = (path_components[0] if len(path_components) == 1 else path_components[-1])
        
    if (file_name.endswith('.prompt') or '.' not in file_name) and os.path.exists(file_path):
        return True
    return False