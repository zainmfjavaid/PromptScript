from typing import List, Tuple
from promptscript.utils.numbers import is_number
from promptscript.utils.debug_level import DebugLevel

PARSER_CONVERSION = {'show':'print_operator', '"':'quote', "'":'quote', '=':'equals', 'load':'load_operator',
                  'save':'save_to_file', 'chat':'chat_operator', 'draw':'draw_operator', 
                  'listen':'listen_operator', 'if': 'if_conditional', 'elif': 'elif_conditional', 
                  'else': 'else_conditional', 'for': 'for_loop', 'in': 'in_operator', 'while': 'while_loop',
                  ']': 'chain_close', 'yield': 'yield_operator'}
INTERPRETER_CONVERSION = {'print_operator':'print(', 'load_operator':'get_environment_variable(', 
                          'save_to_file':'save_to_file(', 'equals':'=', 'chat_operator':'route_chat(',
                          'draw_operator':'route_draw(', 'listen_operator':'route_listen(', 
                          'if_conditional': 'if ', 'elif_conditional': 'elif ', 'else_conditional': 'else',
                          'for_loop': 'for ', 'in_operator': ' in ', 'while_loop': 'while ', 'chain_close': ')',
                          'yield_operator': 'yield_output('}
STANDALONE_CHARACTERS = ['=', '\t', ':', ']', '\n']
PROTECTED_BLOCK_CHARACTERS = ['"', "'"]
OPERATOR_CHARACTERS = ['+', '-', '*', '/']
NEW_PART_CHARACTERS = [' ', '[']


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
    
    parsed_operations = []
    is_open = False
    for i, part in enumerate(parts):
        try:
            if part.lower() in PROTECTED_BLOCK_CHARACTERS:
                is_open = not is_open
                parse_operation = (PARSER_CONVERSION[part.lower()], part.lower())
            elif is_open:
                parse_operation = ('msg', part)
            elif is_number(part) and not is_open:
                parse_operation = ('num', part)
            elif not is_open and part.lower() not in PARSER_CONVERSION:
                parse_operation = ('var', part)
            else:
                parse_operation = (PARSER_CONVERSION[part.lower()], part.lower())
                
            parsed_operations.append(parse_operation)
        except KeyError:
            if DEBUG_LEVEL <= DebugLevel.ERROR:
                raise SyntaxError(f"SYNTAX ERROR: Unexpected token '{part}'")
            
    if DEBUG_LEVEL <= DebugLevel.DEBUG:
        print(f'PARSED PARTS :: {parsed_operations}')
        
    return parsed_operations

def interpret(command: str, DEBUG_LEVEL: DebugLevel=DebugLevel.INFO) -> str:
    parsed_operations = parse(command, DEBUG_LEVEL)

    interpreted_commands = []
    current_interpreted_command = ''
    for op_name, part in parsed_operations:
        conversion = INTERPRETER_CONVERSION.get(op_name, part)
        if conversion == '\n':
            interpreted_commands.append(current_interpreted_command)
            current_interpreted_command = ''
            continue
        else:
            current_interpreted_command += str(conversion)
    if current_interpreted_command:
        interpreted_commands.append(current_interpreted_command)
    
    for i, interpreted_command in enumerate(interpreted_commands):
        for _ in range(interpreted_command.count('(') - interpreted_command.count(')')):
            interpreted_commands[i] += ')'
        
    if DEBUG_LEVEL <= DebugLevel.DEBUG:
        print(f'INTERPRETED COMMANDS :: {interpreted_commands}')
        
    return '\n'.join(interpreted_commands)