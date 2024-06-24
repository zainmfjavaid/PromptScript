import os
from typing import List, Any
from utils.save import save_to_file
from ai.chat_router import route_chat
from ai.draw_router import route_draw
from ai.listen_router import route_listen
from interpreter import interpret
from utils.debug_level import DebugLevel
from utils.is_valid_file import is_promptscript_file


DEBUG_LEVEL = DebugLevel.INFO
environment_scope = {}

def read_file(file_path: str) -> List[str]:
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r') as f:
        return [line.strip('\n').replace('    ', '\t') for line in f.readlines() if line.strip().strip('\n') != '']
    
def get_environment_file_path(file_path: str) -> str:
    return f'{os.path.splitext(file_path)[0]}.env.prompt'
    
def populate_environment(environment_commands: List[str]) -> None:
    for command in environment_commands:
        interpreted_command = interpret(command)
        exec(interpreted_command, globals(), environment_scope)
        
def get_environment_variable(key: str) -> Any:
    if key in environment_scope:
        return environment_scope[key]
    raise KeyError(f"'{key}'")
            
def interpet_file(file_path: str):
    if not is_promptscript_file(file_path):
        raise Exception("Unsupported file type")
    commands = read_file(file_path)
    environment_commands = read_file(get_environment_file_path(file_path))
    
    local_scope = {}
    
    if environment_commands:
        for command in environment_commands:
            interpreted_command = interpret(command)
            exec(interpreted_command, globals(), environment_scope)

    interpreted_commands = []
    for command in commands:
        interpreted_command = interpret(command, DEBUG_LEVEL)
        interpreted_commands.append(interpreted_command)

    combined_commands = '\n'.join(interpreted_commands)
    exec(combined_commands, globals(), local_scope)

if __name__ == '__main__':
    interpet_file()