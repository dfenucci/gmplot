### Configuration file for the Sphinx documentation builder.
###
### NOTE: This requires Python 3 - otherwise, we can't build Markdown docs nor
###       autogenerate documentation from source code.

# Set up the path:
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Configure base functionality:
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_markdown_builder',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'Home'
highlight_language = 'python3'

# Configure extensions:
autoclass_content = 'both'

# Autogenerate source documentation and a sidebar file to be consumed by Sphinx and the GitHub Wiki respectively:
import gmplot
from gmplot.utility import _get_fresh_path, _write_to_sidebar, _GenerateDocFiles

with open('%s/_Sidebar.md' % (_get_fresh_path('_build')), 'w') as file:
    # Add the root documentation file to _Sidebar:
    _write_to_sidebar(file, master_doc)

    # Autogenerate documentation files and update _Sidebar:
    source_ext = _GenerateDocFiles(gmplot, _get_fresh_path('_api'), file)()
    
    # If the file extension of the autogenerated files isn't already in `source_suffix`, add it:
    if source_ext not in source_suffix:
        source_suffix.append(source_ext)

# Copy images into Sphinx source folder:
from distutils.dir_util import copy_tree
copy_tree('images/', '_api/')
