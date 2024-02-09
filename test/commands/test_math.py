from _test_command_base import run_command

# Addition
assert run_command('SHOW 1+1').stdout.strip('\n') == '2'
assert run_command('SHOW 1+ 2').stdout.strip('\n') == '3'
assert run_command('SHOW 1 +2').stdout.strip('\n') == '3'
assert run_command('SHOW 1 + 2').stdout.strip('\n') == '3'

# Subtraction
assert run_command('SHOW 5-1').stdout.strip('\n') == '4'
assert run_command('SHOW 5- 2').stdout.strip('\n') == '3'
assert run_command('SHOW 5 -2').stdout.strip('\n') == '3'
assert run_command('SHOW 5 - 2').stdout.strip('\n') == '3'
assert run_command('SHOW 2 - 5').stdout.strip('\n') == '-3'

# Multiplication
assert run_command('SHOW 5*2').stdout.strip('\n') == '10'
assert run_command('SHOW 5* 2').stdout.strip('\n') == '10'
assert run_command('SHOW 5 *2').stdout.strip('\n') == '10'
assert run_command('SHOW 5 * 2').stdout.strip('\n') == '10'
assert run_command('SHOW 5 * -2').stdout.strip('\n') == '-10'
assert run_command('SHOW 5 * 0').stdout.strip('\n') == '0'

# Division
assert run_command('SHOW 10/2').stdout.strip('\n') == '5.0'
assert run_command('SHOW 10/ 2').stdout.strip('\n') == '5.0'
assert run_command('SHOW 10 /2').stdout.strip('\n') == '5.0'
assert run_command('SHOW 10 / 2').stdout.strip('\n') == '5.0'
assert run_command('SHOW 0 / 2').stdout.strip('\n') == '0.0'
assert run_command('SHOW 10 / 0').stderr != ''