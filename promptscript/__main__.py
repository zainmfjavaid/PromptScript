import sys
from promptscript.cli import run_cli
from promptscript.executor import FileExecutor

def main():
    if len(sys.argv) == 1:
        run_cli()
    else:
        FileExecutor().run(sys.argv[1], **dict(arg.split('=') for arg in sys.argv[2:]))

if __name__ == '__main__':
    main()