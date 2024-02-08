from typing import List

### CURRENT SUPPORTED COMMANDS:
# SHOW "{message}"

OPERATION_WORDS = ['show']
PROTECTED_BLOCK_CHARACTERS = ['"', '"', '"']
NEW_PART_CHARACTERS = [' ']


def lex(command: str) -> List[str]:
    parts = []
    current_block = ''
    is_protected_block = False
    for i, char in enumerate(command):
        if char in PROTECTED_BLOCK_CHARACTERS:
            if not is_protected_block:
                is_protected_block = True
                parts.append(char)
            else:
                is_protected_block = False
                parts.append(current_block)
                parts.append(char)
                current_block = ''
        
        elif char not in NEW_PART_CHARACTERS:
            current_block += char
        
        elif char in NEW_PART_CHARACTERS:
            if not is_protected_block:
                parts.append(current_block)
                current_block = ''
            else:
                current_block += char
    if len(current_block) != 0:
        parts.append(current_block)
            
    return parts