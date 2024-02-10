import os

def get_environment_file_path(file_path: str) -> str:
    return f'{os.path.splitext(file_path)[0]}.env.prompt'

if __name__ == '__main__':
    print(get_environment_file_path('/Users/zainj/PrompScript/promptscript/test/files/test.prompt'))