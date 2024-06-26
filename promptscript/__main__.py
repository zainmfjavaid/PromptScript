import sys
from promptscript.cli import run_cli
from promptscript.executor import FileExecutor


if __name__ == '__main__':
    if len(sys.argv) == 1:
        run_cli()
    else:
        FileExecutor().run(sys.argv[1], **dict(arg.split('=') for arg in sys.argv[2:]))