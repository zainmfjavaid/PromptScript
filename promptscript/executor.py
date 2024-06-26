from typing import Dict, Any

from promptscript.ai.chat_router import route_chat
from promptscript.ai.draw_router import route_draw
from promptscript.ai.listen_router import route_listen

from promptscript.interpreter import interpret
from promptscript.utils.debug_level import DebugLevel
from promptscript.utils.config import ILLEGAL_PARAMETER_NAMES
from promptscript.utils.file import save_to_file, read_file_lines, get_environment_file_path, is_promptscript_file

DEBUG_LEVEL = DebugLevel.INFO

class BaseExecutor:    
    def validate_parameters(self, parameters: Dict):
        for key_name in parameters:
            if key_name in ILLEGAL_PARAMETER_NAMES:
                raise ValueError(f"Illegal parameter name '{key_name}'")

class FileExecutor(BaseExecutor):
    """Class for running and getting the yielded output from PromptScript files"""
    
    def run(self, file_path: str, **kwargs) -> Dict[str, Any]:
        """Executes PromptScript file

        Args:
            file_path (str): Path to PromptScript file

        Returns:
            Dict: Yielded output
        """
        environment_scope, local_scope, output = {}, {}, {}
        
        self.validate_parameters(kwargs)
        local_scope.update(kwargs)
        
        def get_environment_variable(key: str) -> Any:
            if key in environment_scope:
                return environment_scope[key]
            raise KeyError(f"'{key}' not found in environment")
        
        local_scope['yield_output'] = lambda k, v: output.update({k: v})
        local_scope['get_environment_variable'] = get_environment_variable

        if not is_promptscript_file(file_path):
            raise Exception('Unsupported file type')
                
        promptscript_commands = read_file_lines(file_path)
        environment_commands = read_file_lines(get_environment_file_path(file_path))
        
        if environment_commands:
            interpreted_env_command = interpret('\n'.join(environment_commands), DEBUG_LEVEL)
            exec(interpreted_env_command, globals(), environment_scope)
        
        interpreted_commands = []
        for command in promptscript_commands:
            interpreted_command = interpret(command, DEBUG_LEVEL)
            interpreted_commands.append(interpreted_command)

        combined_commands = '\n'.join(interpreted_commands)
        exec(combined_commands, globals(), local_scope)
        
        return output
    
class CommandExecutor(BaseExecutor):
    """Class for running individual PromptScript commands"""

    @staticmethod
    def _get_environment_variable(key: str):
        """Raises error if environment operations are run outside of files."""
        raise NotImplementedError('Environment operations are only avaliable in files.')
    
    def run(self, command: str, **kwargs) -> Dict[str, Any]:
        """Executes individual PromptScript command

        Args:
            command (str): PromptScript command

        Returns:
            Dict: Yielded output
        """
        local_scope, output = {}, {}
        
        self.validate_parameters(kwargs)
        local_scope.update(kwargs)
        
        local_scope['yield_output'] = lambda k, v: output.update({k: v})
        local_scope['get_environment_variable'] = CommandExecutor._get_environment_variable
        
        interpreted_command = interpret(command, DEBUG_LEVEL)
        exec(interpreted_command, globals(), local_scope)
        
        return output
    
class PersistentCommandExecutor(BaseExecutor):
    """Class for running PromptScript commands with context persisting between runs"""
    
    def __init__(self):
        self.local_scope = {}
        self.local_scope['get_environment_variable'] = CommandExecutor._get_environment_variable
        
    def run(self, command: str, **kwargs) -> Dict[str, Any]:
        output = {}
        
        self.validate_parameters(kwargs)
        self.local_scope.update(kwargs)
        
        self.local_scope['yield_output'] = lambda k, v: output.update({k: v})
        
        interpreted_command = interpret(command, DEBUG_LEVEL)
        exec(interpreted_command, globals(), self.local_scope)
        
        return output