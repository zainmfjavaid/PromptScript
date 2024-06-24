from utils.save import save_to_file
from interpreter import interpret
from utils.debug_level import DebugLevel
from ai.chat_router import route_chat
from ai.draw_router import route_draw
from ai.listen_router import route_listen

local_scope = {}
DEBUG_LEVEL = DebugLevel.INFO

def run_cli():
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

        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting...")
            break

        except Exception as e:
            print(f'Error: {e}')