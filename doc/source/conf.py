import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

import sphinx_rtd_theme
import send_nsca

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = []
extensions += ['sphinx.ext.autodoc']
extensions += ['sphinx.ext.intersphinx']
extensions += ['sphinx.ext.viewcode']
extensions += ['sphinx_autodoc_typehints']

templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

project = u'send_nsca'
copyright = u'2019, Josef Friedrich'
author = u'Josef Friedrich'
version = send_nsca.__version__
release = send_nsca.__version__
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_static_path = []
htmlhelp_basename = 'send_nscadoc'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'show-inheritance': True,
}
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
