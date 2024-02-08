from lexer import lex, parse

while True:
    try:
        print(parse(input('Command: ')))
    except Exception as e:
        raise
    except KeyboardInterrupt:
        break