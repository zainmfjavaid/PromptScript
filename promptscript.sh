#!/bin/bash
SCRIPT_PATH=$(readlink -f "$0" 2>/dev/null) || SCRIPT_PATH=$0
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd 

if [ $# -eq 0 ]; then
    python "$SCRIPT_DIR/promptscript/cli.py"
else
    python "$SCRIPT_DIR/promptscript/file_interpreter.py $1"
fi