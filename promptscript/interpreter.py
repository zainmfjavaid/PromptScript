from typing import List, Tuple
from utils.numbers import is_number
from utils.debug_level import DebugLevel

### CURRENT SUPPORTED COMMANDS:
# SHOW "{message}"

DEBUG_LEVEL = DebugLevel.DEBUG
AST_CONVERSION = {'show':'print_operator', '"':'quote', '=':'equals'}
INTERPRETER_CONVERSION = {'print_operator':'print(', 'equals':'='}
STANDALONE_CHARACTERS = ['=']
PROTECTED_BLOCK_CHARACTERS = ['"', '"', '"']
OPERATOR_CHARACTERS = ['+', '-', '*', '/']
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
                
        elif char in STANDALONE_CHARACTERS:
            if not is_protected_block:
                parts.append(current_block)
                parts.append(char)
                current_block = ''
            else:
                current_block += char
        
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
            
    return [part for part in parts if part != '']

def parse(command: str) -> List[Tuple]:
    parts = lex(command)
    if DEBUG_LEVEL <= DebugLevel.DEBUG:
        print(f'LEXED PARTS :: {parts}')
    
    ast_operations = []
    is_open = False
    for i, part in enumerate(parts):
        try:
            if part.lower() in PROTECTED_BLOCK_CHARACTERS:
                is_open = not is_open
                ast_operation = (AST_CONVERSION[part.lower()], part.lower())
            elif is_open:
                ast_operation = ('msg', part)
            elif is_number(part) and not is_open:
                ast_operation = ('num', part)
            elif not is_open and part.lower() not in AST_CONVERSION:
                if i != len(parts) - 1 and parts[i + 1][0] == '=':                    
                    ast_operation = ('var', part)
                else:
                    raise KeyError
            else:
                ast_operation = (AST_CONVERSION[part.lower()], part.lower())
                
            ast_operations.append(ast_operation)
        except KeyError:
            if DEBUG_LEVEL <= DebugLevel.ERROR:
                raise SyntaxError(f"SYNTAX ERROR: Unexpected token '{part}'")
            
    if DEBUG_LEVEL <= DebugLevel.DEBUG:
        print(f'PARSED PARTS :: {ast_operations}')
        
    return ast_operations

def interpret(command: str):
    ast_operations = parse(command)
    
    interpreted_command = ''
    is_open_paren = False
    for op_name, part in ast_operations:
        conversion = INTERPRETER_CONVERSION.get(op_name, part)

        if '(' in str(conversion):
            is_open_paren = True
        interpreted_command += str(conversion)
        
    if is_open_paren:
        interpreted_command += ')'
        
    if DEBUG_LEVEL <= DebugLevel.DEBUG:
        print(f'INTERPRETED COMMAND :: {interpreted_command}')
        
    return interpreted_command