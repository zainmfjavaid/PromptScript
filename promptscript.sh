#!/bin/bash
SCRIPT_PATH=$(readlink -f "$0" 2>/dev/null) || SCRIPT_PATH=$0
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd "$SCRIPT_DIR"

python promptscript/main.py