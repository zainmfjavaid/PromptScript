import sys
from typing import List
from interpreter import interpret


def read_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        return [line.strip('\n') for line in f.readlines() if line.strip().strip('\t').strip('\n') != '']
    
def interpet_file():
    file_path = sys.argv[1]
    commands = read_file(file_path)
    local_scope = {}

    for command in commands:
        interpreted_command = interpret(command)
        exec(interpreted_command, globals(), local_scope)

if __name__ == '__main__':
    interpet_file()