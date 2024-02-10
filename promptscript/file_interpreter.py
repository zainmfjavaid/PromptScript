import os
import sys
from typing import List, Any
from interpreter import interpret
from utils.debug_level import DebugLevel
from utils.is_valid_file import is_promptscript_file
from environment_management import get_environment_file_path


DEBUG_LEVEL = DebugLevel.DEBUG
environment_scope = {}

def read_file(file_path: str) -> List[str]:
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r') as f:
        return [line.strip('\n') for line in f.readlines() if line.strip().strip('\t').strip('\n') != '']
    
def populate_environment(environment_commands: List[str]) -> None:
    for command in environment_commands:
        interpreted_command = interpret(command)
        exec(interpreted_command, globals(), environment_scope)
        
def get_environment_variable(key: str) -> Any:
    if key in environment_scope:
        return environment_scope[key]
    raise KeyError(f"'{key}'")
            
def interpet_file():
    file_path = sys.argv[1]
    if not is_promptscript_file(file_path):
        raise Exception("Unsupported file type")
    commands = read_file(file_path)
    environment_commands = read_file(get_environment_file_path(file_path))
    
    local_scope = {}
    
    if environment_commands:
        for command in environment_commands:
            interpreted_command = interpret(command)
            exec(interpreted_command, globals(), environment_scope)

    for command in commands:
        interpreted_command = interpret(command, DEBUG_LEVEL, )
        exec(interpreted_command, globals(), local_scope)

if __name__ == '__main__':
    interpet_file()