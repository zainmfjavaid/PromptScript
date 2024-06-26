import atexit
import readline
from promptscript.interpreter import interpret
from promptscript.ai.chat_router import route_chat
from promptscript.ai.draw_router import route_draw
from promptscript.ai.listen_router import route_listen
from promptscript.utils.save import save_to_file
from promptscript.utils.debug_level import DebugLevel

local_scope = {}
DEBUG_LEVEL = DebugLevel.DEBUG
COMMANDS = ['exit', 'save', 'load', 'show', 'chat', 'draw', 'listen', 'if', 'elif', 'else', 'for', 'while']

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
            if text.isupper():
                return options[state].upper()
            else:
                return options[state] 
    
    readline.parse_and_bind('tab: complete')
    readline.set_completer(completer)

def run_cli():
    setup_readline()
    
    in_buffer = False
    command_buffer = []
    while True:
        try:
            if not in_buffer:
                user_input = input('>>> ')
            else:
                user_input = input('... ')
            if user_input.lower() == 'exit':
                break
            
            interpreted_command = interpret(user_input, DEBUG_LEVEL)

            if user_input.lower().startswith(('if', 'elif', 'else')):
                in_buffer = True
            
            if in_buffer:
                if user_input == '':
                    interpreted_command = '\n'.join(command_buffer)
                    in_buffer = False
                else:
                    command_buffer.append(interpreted_command)
            
            if not in_buffer:
                exec(interpreted_command, globals(), local_scope)

            if DEBUG_LEVEL <= DebugLevel.DEBUG:
                print('Local scope:', local_scope)

        except KeyboardInterrupt:
            print('\nKeyboard Interrupt')
        
        except EOFError:
            print("\n\nExiting...")
            break

        except Exception as e:
            print(f'Error: {e}')