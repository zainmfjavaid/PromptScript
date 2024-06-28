import os
import sys
from sphinx.highlighting import lexers

sys.path.insert(0, os.path.abspath('.'))

from promptscript_lexer import PromptScriptLexer

# -- Project information -----------------------------------------------------

project = 'PromptScript'
copyright = '2024, Zain Javaid'
author = 'Zain Javaid'
release = '0.1.2'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------

html_theme = 'shibuya'
html_static_path = ['_static']
html_theme_options = {
    'accent_color': 'jade'
}

def setup(app):
    lexers['promptscript'] = PromptScriptLexer()