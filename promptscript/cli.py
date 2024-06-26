import atexit
import readline
from promptscript.utils.config import COMMANDS
from promptscript.executor import PersistentCommandExecutor


def setup_readline():
    history_file = '.cli_history'
    try:
        readline.read_history_file(history_file)
    except FileNotFoundError:
        pass
    readline.set_history_length(1000)

    atexit.register(readline.write_history_file, history_file)

    def completer(text: str, state: int):
        options = [cmd for cmd in COMMANDS if cmd.startswith(text.lower())]
        if state < len(options):
            if text == '':
                return '\t'
            
            if text.isupper():
                return options[state].upper()
            else:
                return options[state] 
    
    readline.parse_and_bind('tab: complete')
    readline.set_completer(completer)

def run_cli():
    command_executor = PersistentCommandExecutor()
    setup_readline()
    
    in_buffer = False
    command_buffer = []
    while True:
        try:
            if not in_buffer:
                command = input('>>> ')
            else:
                command = input('... ')
            if command.lower() == 'exit':
                break
            
            if command.lower().startswith(('if', 'elif', 'else')):
                in_buffer = True
            
            if in_buffer:
                if command == '':
                    command = '\n'.join(command_buffer)
                    in_buffer = False
                else:
                    command_buffer.append(command)
            
            if not in_buffer:
                command_executor.run(command)

        except KeyboardInterrupt:
            print('\nKeyboard Interrupt')
        
        except EOFError:
            print("\n\nExiting...")
            break

        except Exception as e:
            print(f'Error: {e}')