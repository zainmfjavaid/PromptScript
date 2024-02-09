import os
import sys
import subprocess
from typing import List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'promptscript')))

from interpreter import interpret


def run_command(command: str) -> subprocess.CompletedProcess:
    interpreted_command = interpret(command)
    subprocess_command = ['python', '-c', interpreted_command]
    output = subprocess.run(subprocess_command, capture_output=True, text=True)
    
    return output

def run_environment_command(command: str) -> subprocess.CompletedProcess:
    interpreted_command = interpret(command)
    local_scope = {}

    exec(interpreted_command, globals(), local_scope)
    return local_scope    