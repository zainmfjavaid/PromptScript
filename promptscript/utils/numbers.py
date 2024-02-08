def is_number(string: str) -> bool:
    is_dot = False
    for character in string:
        if character == '.':
            if is_dot:
                return False
            else:
                is_dot = True
        elif not character.isdigit():
            return False
    return True