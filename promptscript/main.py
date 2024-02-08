import subprocess
from interpreter import interpret

while True:
    try:
        interpreted_command = interpret(input('Command: '))
        subprocess_command = ['python', '-c', interpreted_command]
        output = subprocess.run(subprocess_command, capture_output=True, text=True)
        if output.stderr:
            print('RUNTIME ERROR:', output.stderr)
        else:
            print(f'Output :: {output.stdout}')
        
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        break