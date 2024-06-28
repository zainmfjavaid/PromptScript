from pygments.lexer import RegexLexer
from pygments.token import Text, Keyword, Name

class PromptScriptLexer(RegexLexer):
    name = 'PromptScript'
    aliases = ['promptscript']
    filenames = ['*.prompt']

    tokens = {
        'root': [
            (r'\b(show|chat|draw|listen|save|yield|if|elif|else|for|while|load)\b', Keyword),
            (r'\b(prompt|model|api_key)\b', Name.Variable),
            (r'.', Text),
        ],
    }