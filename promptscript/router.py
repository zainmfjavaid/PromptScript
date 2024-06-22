import sys
from cli import run_cli
from file_interpreter import interpet_file

if len(sys.argv) == 1:
    run_cli()
else:
    interpet_file(sys.argv[1])