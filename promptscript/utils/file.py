import os
from typing import List

# For the 'save' operator
def save_to_file(value: str, file_path: str):
    with open(file_path, 'w') as f:
        f.write(value)
        
# Helpers
def is_promptscript_file(file_path: str) -> bool:
    path_components = file_path.split('/')
    file_name = (path_components[0] if len(path_components) == 1 else path_components[-1])
        
    if (file_name.endswith('.prompt') or '.' not in file_name) and os.path.exists(file_path):
        return True
    return False

def get_environment_file_path(file_path: str) -> str:
    return f'{os.path.splitext(file_path)[0]}.env.prompt'

def read_file_lines(file_path: str) -> List[str]:
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r') as f:
        return [line.strip('\n').replace('    ', '\t') for line in f.readlines() if line.strip().strip('\n') != '']