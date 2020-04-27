# -*- coding: utf-8 -*-

import os
import sys
import re
from recommonmark.parser import CommonMarkParser
import sphinx_rtd_theme
import recommonmark
from recommonmark.transform import AutoStructify

# -- Path setup --------------------------------------------------------------

if not 'READTHEDOCS' in os.environ:
    sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..src/'))
sys.path.append(os.path.abspath('.Keras/'))
sys.path.append(os.path.abspath('.Keras-models/'))
sys.path.append(os.path.abspath('.Tensorflow/'))
sys.path.append(os.path.abspath('.Tensorflow-models/'))
sys.path.append(os.path.abspath('.TF-keras/'))
sys.path.append(os.path.abspath('.deeplearning/'))
sys.path.append(os.path.abspath('.Pytorch/'))
sys.path.append(os.path.abspath('.Numpy/'))
sys.path.append(os.path.abspath('.MXNet/'))

# -- Project information -----------------------------------------------------

project = 'Scripts'
slug = re.sub(r'\W+', '-', project.lower())
author = 'wangzf'
copyright = "2020 wangzf"
version = "1.0"
release = version
language = 'zh-cn'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
    'sphinx.ext.mathjax',
    # 'sphinx.ext.apidoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    # 'nbsphinx',
    # 'sphinx_markdown_tables'
    # 'recommonmark',
]
templates_path = ['_templates']
# source_parsers = {
#     '.md': CommonMarkParser,
# }
# source_suffix = [
#     '.rst',
#     '.md',
# ]
exclude_patterns = ['**.ipynb_checkpoints']
master_doc = 'index'


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_elements={# The paper size ('letterpaper' or 'a4paper').
    'papersize':'a4paper',# The font size ('10pt', '11pt' or '12pt').
    'pointsize':'12pt','classoptions':',oneside','babel':'',#必須
    'inputenc':'',#必須
    'utf8extra':'',#必須
    # Additional stuff for the LaTeX preamble.
    'preamble': r"""
    \usepackage{xeCJK}
    \usepackage{indentfirst}
    \setlength{\parindent}{2em}
    \setCJKmainfont{WenQuanYi Micro Hei}
    \setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
    \setCJKfamilyfont{song}{WenQuanYi Micro Hei}
    \setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
    \XeTeXlinebreaklocale "zh"
    \XeTeXlinebreakskip = 0pt plus 1pt
    """
}


def setup(app):
    app.add_config_value('recommonmark_config', {
        # 'url_resolver': lambda url: github_doc_root + url,
        'enable_math': False,
        'enable_inline_math': False,
    }, True)
    app.add_transform(AutoStructify)