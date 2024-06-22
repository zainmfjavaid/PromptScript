#!/bin/bash
ALIAS_NAME='promptscript'
ALIAS_COMMAND="python3 $PWD/promptscript/router.py"

if [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG_FILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG_FILE="$HOME/.bash_profile"
else
    echo "Unsupported shell. Please add the alias manually to your shell configuration file."
    exit 1
fi

if grep -q "alias $ALIAS_NAME=" "$SHELL_CONFIG_FILE"; then
    echo "Alias '$ALIAS_NAME' already exists in $SHELL_CONFIG_FILE"
else
    echo "Adding alias to $SHELL_CONFIG_FILE"
    echo "alias $ALIAS_NAME='$ALIAS_COMMAND'" >> "$SHELL_CONFIG_FILE"
  
    source "$SHELL_CONFIG_FILE"
    echo "Alias '$ALIAS_NAME' added and applied. You can now use PromptScript from the terminal."
fi