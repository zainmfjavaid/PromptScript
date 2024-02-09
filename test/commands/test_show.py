from _test_command_base import run_command


assert run_command('SHOW "Hello, World!"').stdout.strip('\n') == 'Hello, World!'
assert run_command('SHOW 5').stdout.strip('\n') == '5'