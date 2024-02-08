from lexer import lex

while True:
    try:
        print(lex(input('Command: ')))
    except Exception as e:
        raise
    except KeyboardInterrupt:
        break