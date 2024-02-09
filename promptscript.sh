#!/bin/bash
SCRIPT_PATH=$(readlink -f "$0" 2>/dev/null) || SCRIPT_PATH=$0
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd "$SCRIPT_DIR"

if [ $# -eq 0 ]; then
    python promptscript/cli.py
else
    python promptscript/file_interpreter.py "$1"
fi