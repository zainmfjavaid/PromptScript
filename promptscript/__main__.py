import sys
from promptscript.cli import run_cli
from promptscript.file_interpreter import interpet_file


if __name__ == '__main__':
    if len(sys.argv) == 1:
        run_cli()
    else:
        interpet_file(sys.argv[1])