def save_to_file(value: str, file_path: str):
    with open(file_path, 'w') as f:
        f.write(value)