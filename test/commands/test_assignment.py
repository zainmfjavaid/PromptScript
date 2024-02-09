from _test_command_base import run_environment_command


assert run_environment_command('x = 5')['x'] == 5
assert run_environment_command('x = "Hello, World!"')['x'] == 'Hello, World!'
assert run_environment_command('x = 0.01')['x'] == 0.01