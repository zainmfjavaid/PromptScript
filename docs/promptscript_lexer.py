from pygments.lexer import RegexLexer
from pygments.token import Text, Keyword, Name, String, Number, Comment

class PromptScriptLexer(RegexLexer):
    name = 'PromptScript'
    aliases = ['promptscript']
    filenames = ['*.prompt']

    tokens = {
        'root': [
            (r'\b(if|elif|else|for|while|in)\b', Keyword),
            (r'\b(show|chat|draw|listen|save|yield|load|read)\b', Name.Builtin),
            (r'\b(prompt|model|api_key)\b', Name.Variable),
            (r'"[^"\\]*(?:\\.[^"\\]*)*"', String),
            (r'\b\d+\b', Number),
            (r'#.*', Comment.Single),
            (r'.', Text)
        ],
    }