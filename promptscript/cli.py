from utils.save import save_to_file
from interpreter import interpret
from utils.debug_level import DebugLevel

local_scope = {}
DEBUG_LEVEL = DebugLevel.DEBUG

while True:
    try:
        user_input = input('Command: ')
        if user_input.lower() == 'exit':
            break
        
        interpreted_command = interpret(user_input, DEBUG_LEVEL)
        exec(interpreted_command, globals(), local_scope)

        if DEBUG_LEVEL <= DebugLevel.DEBUG:
            print('Local scope:', local_scope)

    except Exception as e:
        print(f'Error: {e}')
        
    except KeyboardInterrupt:
        print("\n\nExiting...")
        break