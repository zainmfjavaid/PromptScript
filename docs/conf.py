import os
import sys
from dotenv import load_dotenv
from sphinx.highlighting import lexers

sys.path.insert(0, os.path.abspath('.'))

from promptscript_lexer import PromptScriptLexer

load_dotenv('config.env')

# -- Project information -----------------------------------------------------

project = 'PromptScript'
copyright = '2024, Zain Javaid'
author = 'Zain Javaid'
release = '0.3.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_design',
    'sphinx_tabs.tabs',
    'sphinx_docsearch'
]

sitemap_excludes = ['404/']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'shibuya'
html_static_path = ['_static']
html_favicon = '_static/favicon.ico'
html_title = 'PromptScript Documentation'
html_theme_options = {
    'accent_color': 'jade',
    'globaltoc_expand_depth': 1,
    'github_url': 'https://github.com/zainmfjavaid/PromptScript',
    'nav_links': [
        {
            'title': 'About',
            'url': 'about'
        }
    ]
}

if os.getenv('USE_DOCSEARCH'):
    docsearch_app_id = os.environ['DOCSEARCH_APP_ID']
    docsearch_api_key = os.environ['DOCSEARCH_API_KEY']
    docsearch_index_name = os.environ['DOCSEARCH_INDEX_NAME']

def setup(app):
    lexers['promptscript'] = PromptScriptLexer()