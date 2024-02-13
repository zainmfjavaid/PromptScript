from typing import List, Tuple
from utils.numbers import is_number
from utils.debug_level import DebugLevel

### CURRENT SUPPORTED COMMANDS:
# Variable assignment (x = 5, x = "hello", etc)
# Printing (SHOW "msg", SHOW variable)
# Math operations (+, -, *, /)

AST_CONVERSION = {'show':'print_operator', '"':'quote', "'":'quote', '=':'equals', 'use':'load_operator',
                  'save':'save_to_file', '->':'location_operator', 'with':'with_operator',
                  'chat':'chat_operator'}
INTERPRETER_CONVERSION = {'print_operator':'print(', 'load_operator':'get_environment_variable(', 
                          'save_to_file':'save_to_file(', 'location_operator':',', 'equals':'=',
                          'with_operator':'(', 'chat_operator':'route_chat'}
STANDALONE_CHARACTERS = ['=']
PROTECTED_BLOCK_CHARACTERS = ['"', "'"]
OPERATOR_CHARACTERS = ['+', '-', '*', '/']
NEW_PART_CHARACTERS = [' ']


def lex(command: str, DEBUG_LEVEL: DebugLevel) -> List[str]:
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
    parts = [part for part in parts if part != '']
    
    if DEBUG_LEVEL <= DebugLevel.DEBUG:
        print(f'LEXED PARTS :: {parts}')
    
    return parts

def parse(command: str, DEBUG_LEVEL: DebugLevel) -> List[Tuple]:
    parts = lex(command, DEBUG_LEVEL)
    
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
                ast_operation = ('var', part)
            else:
                ast_operation = (AST_CONVERSION[part.lower()], part.lower())
                
            ast_operations.append(ast_operation)
        except KeyError:
            if DEBUG_LEVEL <= DebugLevel.ERROR:
                raise SyntaxError(f"SYNTAX ERROR: Unexpected token '{part}'")
            
    if DEBUG_LEVEL <= DebugLevel.DEBUG:
        print(f'PARSED PARTS :: {ast_operations}')
        
    return ast_operations

def interpret(command: str, DEBUG_LEVEL: DebugLevel=DebugLevel.INFO) -> str:
    ast_operations = parse(command, DEBUG_LEVEL)
    
    interpreted_command = ''
    open_paren_count = 0
    for op_name, part in ast_operations:
        conversion = INTERPRETER_CONVERSION.get(op_name, part)

        if '(' in conversion and ')' not in conversion:
            open_paren_count += 1
        interpreted_command += str(conversion)
        
    for _ in range(open_paren_count):
        interpreted_command += ')'
        
    if DEBUG_LEVEL <= DebugLevel.DEBUG:
        print(f'INTERPRETED COMMAND :: {interpreted_command}')
        
    return interpreted_command