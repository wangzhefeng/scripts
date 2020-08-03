.. _header-n0sphinx:

Sphinx Doc
================

Sphinx is a powerful documentation generator that has many great
features for writing technical documentation including:

-  Generate web pages, printable PDFs, documents for e-readers (ePub),
   and more all from the same sources

-  You can use reStructuredText or Markdown to write documentation

-  An extensive system of cross-referencing code and documentation

-  Syntax highlighted code samples

-  A vibrant ecosystem of first and third-party
   `extensions <https://www.sphinx-doc.org/en/master/usage/extensions/index.html#builtin-sphinx-extensions>`__

.. _header-n15sphinx:

1.安装环境
----------

（1）激活 Python 虚拟环境

.. code:: shell

   workon doc_env

（2）安装 Sphinx 及其依赖库

.. code:: shell

   $ pip3 install sphinx 
   $ pip3 install sphinx-autobuild 
   $ pip3 install sphinx_rtd_theme

.. _header-n20sphinx:

2.创建文档
----------

（1）创建 Sphinx Doc 项目目录

.. code:: shell

   $ mkdir project
   $ cd project
   $ mkdir docs
   $ mkdir src
   $ cd docs

（2）创建 Sphinx 项目

.. code:: shell

   $ sphinx quickstart

.. _header-n25sphinx:

3.修改配置文件
--------------

.. _header-n26sphinx:

3.1 更改主题
~~~~~~~~~~~~

.. code:: python

   # ./project/docs/source/conf.py

   import sphinx_rtd_theme

   html_theme = "sphinx_rtd_theme"
   html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

.. _header-n28sphinx:

3.2 支持 markdown 语法
~~~~~~~~~~~~~~~~~~~~~~

（1）安装扩展库：

.. code:: shell

   $ pip3 install recommonmark

（2）修改配置：

.. code:: python

   # ./project/doca/source/conf.py

   from recommonmark.parser import CommonMarkParser

   extensions = [
       "recommonmark",
   ]

   source_parsers = {
       '.md': CommonMarkParser,
   }

   source_suffix = ['.rst', '.md']

.. _header-n33sphinx:

4.编译文档:
-----------

.. code:: shell

   cd ./project/docs/
   make html

.. _header-n35sphinx:

5.GitHub 代码托管:
------------------

.. code:: shell

   cd ./project/
   touch .gitignore

   git init
   git add doc
   git remote add origin git:/github.git
   git push -u origin master

.. _header-n37sphinx:

6.绑定 Read the Docs:
---------------------

1. `Import your
   docs. <https://docs.readthedocs.io/en/stable/intro/import-guide.html>`__

2. `Read the Docs dashboard <https://readthedocs.org/dashboard/>`__

3. `Import <https://readthedocs.org/dashboard/import/?__cf_chl_captcha_tk__=f51d0fd05a6dd27a26845c9bd923a6f42ecfded4-1588260812-0-AVHp7xZY-MfpUWYf-sWQgn7MpabCmi2Dzc_tn4_f3tGxMObBh87mGw19KwybY3HkO9EzmoByZ_vpqhjdGT6oOoXXPt714nvln3sxrf6vsoIa_Q8wQ0aHNgzPEhBiO7u0LyHFxtYsg8cbCFpUY-Y_HPZ-Th-S6BmRj6pZIZPh4ieiR6nrWAmQEqnhPeCl79jRC11MMwJ5Gao4xji5JEufhc98l4D-okayG_5A1B8W2kCEXPaENPFiBc113EpO3E70G03ibg25CfezRwD7jXAG5Sc86TZ_u35SRkn7e_IySD-yEkUec8NRFQRPH6uEhP8RPVXdjKzhFrD7D6s19Uevg8eDXqTCO-y8TjdSTQ_28xcDeBz_jMRyveeYFNp5QgGbXRox5WxdaiMFCGaufD4Aqfc>`__

.. _header-n45sphinx:

7.版本管理
----------

-  `Version Doc <https://docs.readthedocs.io/en/stable/versions.html>`__

.. _header-n49sphinx:

8.资源
------

-  `Sphinx documentation <https://www.sphinx-doc.org/en/master/>`__

-  `RestructuredText
   primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__

-  `An introduction to Sphinx and Read the Docs for technical
   writers <https://www.ericholscher.com/blog/2016/jul/1/sphinx-and-rtd-for-writers/>`__

.. _header-n57sphinx:

9.config.py 模板：
------------------

.. code:: python

   # -*- coding: utf-8 -*-
   #
   # Configuration file for the Sphinx documentation builder.
   #
   # This file does only contain a selection of the most common options. For a
   # full list see the documentation:
   # https://www.sphinx-doc.org/en/master/usage/configuration.html

   # -- Path setup --------------------------------------------------------------

   # If extensions (or modules to document with autodoc) are in another directory,
   # add these directories to sys.path here. If the directory is relative to the
   # documentation root, use os.path.abspath to make it absolute, like shown here.
   #
   # import os
   # import sys
   # sys.path.insert(0, os.path.abspath('.'))


   # -- Project information -----------------------------------------------------

   project = 'OpenCV'
   copyright = '2018, Hunag Xinyuan'
   author = 'Hunag Xinyuan'

   # The short X.Y version
   version = '1.0'
   # The full version, including alpha/beta/rc tags
   release = '1.0'


   # -- General configuration ---------------------------------------------------

   # If your documentation needs a minimal Sphinx version, state it here.
   #
   # needs_sphinx = '1.0'

   # Add any Sphinx extension module names here, as strings. They can be
   # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
   # ones.
   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.viewcode',
       'sphinx.ext.todo',
       'sphinx.ext.mathjax',
       'sphinx.ext.apidoc',
       'sphinx.ext.extlinks',
       'nbsphinx',
       'sphinx_markdown_tables',
       'sphinx.ext.githubpages',
   ]

   # Add any paths that contain templates here, relative to this directory.
   templates_path = ['_templates']

   # The suffix(es) of source filenames.
   # You can specify multiple suffix as a list of string:
   #
   # source_suffix = ['.rst', '.md']
   # source_suffix = '.rst'

   # The master toctree document.
   master_doc = 'index'

   # The language for content autogenerated by Sphinx. Refer to documentation
   # for a list of supported languages.
   #
   # This is also used if you do content translation via gettext catalogs.
   # Usually you set "language" from the command line for these cases.
   language = 'zh_CN'

   # List of patterns, relative to source directory, that match files and
   # directories to ignore when looking for source files.
   # This pattern also affects html_static_path and html_extra_path.
   exclude_patterns = [
       '**.ipynb_checkpoints',
   ]

   # The name of the Pygments (syntax highlighting) style to use.
   pygments_style = None


   # -- Options for HTML output -------------------------------------------------

   # The theme to use for HTML and HTML Help pages.  See the documentation for
   # a list of builtin themes.
   #
   import sphinx_rtd_theme
   html_theme = 'sphinx_rtd_theme'
   html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

   # Theme options are theme-specific and customize the look and feel of a theme
   # further.  For a list of options available for each theme, see the
   # documentation.
   #
   # html_theme_options = {}

   # Add any paths that contain custom static files (such as style sheets) here,
   # relative to this directory. They are copied after the builtin static files,
   # so a file named "default.css" will overwrite the builtin "default.css".
   html_static_path = ['_static']

   # Custom sidebar templates, must be a dictionary that maps document names
   # to template names.
   #
   # The default sidebars (for documents that don't match any pattern) are
   # defined by theme itself.  Builtin themes are using these templates by
   # default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
   # 'searchbox.html']``.
   #
   # html_sidebars = {}


   # Markdown support
   import recommonmark
   from recommonmark.transform import AutoStructify
   from recommonmark.parser import CommonMarkParser
   source_parsers = {
       # '.md': CommonMarkParser,
       '.md': 'recommonmark.parser.CommonMarkParser',
   }
   source_suffix = ['.rst', '.md']


   def setup(app):
       app.add_config_value('recommonmark_config', {
           # 'url_resolver': lambda url: github_doc_root + url,
           'enable_math': False,
           'enable_inline_math': False,
       }, True)
       app.add_transform(AutoStructify)


   # math support
   # TODO


   # -- Options for HTMLHelp output ---------------------------------------------

   # Output file base name for HTML help builder.
   htmlhelp_basename = 'OpenCVdoc'


   # -- Options for manual page output ------------------------------------------

   # One entry per manual page. List of tuples
   # (source start file, name, description, authors, manual section).
   # man_pages = [
   #     (master_doc, 'opencv', u'OpenCV Documentation',
   #     [author], 1)
   # ]


   # -- Options for Texinfo output ----------------------------------------------

   # Grouping the document tree into Texinfo files. List of tuples
   # (source start file, target name, title, author,
   #  dir menu entry, description, category)
   # texinfo_documents = [
   #     (master_doc, 'OpenCV', u'OpenCV Documentation',
   #      author, 'OpenCV', 'One line description of project.',
   #      'Miscellaneous'),
   # ]


   # -- Options for Epub output -------------------------------------------------

   # Bibliographic Dublin Core info.
   # epub_title = project

   # The unique identifier of the text. This can be a ISBN number
   # or the project homepage.
   #
   # epub_identifier = ''

   # A unique identification for the text.
   #
   # epub_uid = ''

   # A list of files that should not be packed into the epub file.
   # epub_exclude_files = ['search.html']


   # -- Extension configuration -------------------------------------------------


   # -- Options for LaTeX output ------------------------------------------------

   # latex_elements={
   #     # The paper size ('letterpaper' or 'a4paper').
   #     'papersize': 'a4paper', # The font size ('10pt', '11pt' or '12pt').
   #     'pointsize': '12pt',
   #     'classoptions': ',oneside',
   #     'babel': '',    #必須
   #     'inputenc': '', #必須
   #     'utf8extra': '',#必須
   #     # Additional stuff for the LaTeX preamble.
   #     'preamble': r"""
   #         \usepackage{xeCJK}
   #         \usepackage{indentfirst}
   #         \setlength{\parindent}{2em}
   #         \setCJKmainfont{WenQuanYi Micro Hei}
   #         \setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
   #         \setCJKfamilyfont{song}{WenQuanYi Micro Hei}
   #         \setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
   #         \XeTeXlinebreaklocale "zh"
   #         \XeTeXlinebreakskip = 0pt plus 1pt
   #     """
   # }


10.reStructuredText Markup 语法
------------------------------------

:reStructured: https://docutils.sourceforge.io/rst.html
:A ReStructuredText Primer: https://docutils.sourceforge.io/docs/user/rst/quickstart.html
:Quick reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html
:reStructuredText Markup Specification: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks
:Docutils: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html

10.1 段落
~~~~~~~~~~~~~~~

   Paragraphs contain text and may contain inline markup:
   *emphasis*, **strong emphasis**, `interpreted text`, ``inline
   literals``, standalone hyperlinks (http://www.python.org),
   external hyperlinks (Python_), internal cross-references
   (example_), footnote references ([1]_), citation references
   ([CIT2002]_), substitution references (|example|), and _`inline internal targets`.

   Paragraphs are separated by blank lines and are left-aligned.

.. note::

   知识点:

      - *emphasis*

      - **strong emphasis**

      - `interpreted text`

      - ``inline literals``

      - standalone hyperlinks (http://www.python.org)

      - external hyperlinks(Python_)

      - internal cross-references(example_)

      - footnote references([1]_)

      - citation references([CIT2002]_)

      - substitution references(|example|)

      - _`inline internal targets`


10.2 Lists
~~~~~~~~~~~~~~~

   1.Bullet lists

      - This is a bullet list.

      - Bullets can be "*", "+", or "-".

   2.Enumerated lists

      1. This is an enumerated list.

      2. Enumerators may be arabic numbers, letters, or roman
         numerals.

   3.Definition lists:

      what
         Definition lists associate a term with a definition.

      how
         The term is a one-line phrase, and the definition is one
         or more paragraphs or body elements, indented relative to
         the term.

   4.Field lists:

      :what: Field lists map field names to field bodies, like
            database records.  They are often part of an extension
            syntax.

      :how: The field marker is a colon, the field name, and a
            colon.

            The field body may contain one or more body elements,
            indented relative to the field marker.

   5.Option lists, for listing command-line options:

      -a            command-line option "a"
      -b file       options can have arguments
                  and long descriptions
      --long        options can be long also
      --input=file  long options can also have
                  arguments
      /V            DOS/VMS-style options too

   .. note:: 

      There must be at least two spaces between the option and the description.


10.3 Literal blocks:
~~~~~~~~~~~~~~~~~~~~~~~~

   Literal blocks are either indented or line-prefix-quoted blocks,
   and indicated with a double-colon ("::") at the end of the
   preceding paragraph (right here -->)::

      if literal_block:
         text = 'is left as-is'
         spaces_and_linebreaks = 'are preserved'
         markup_processing = None

10.4 Block quotes:
~~~~~~~~~~~~~~~~~~

   Block quotes consist of indented body elements:

      This theory, that is mine, is mine.

      -- Anne Elk (Miss)

10.5 Doctest blocks:
~~~~~~~~~~~~~~~~~~~~~~~

   >>> print 'Python-specific usage examples; begun with ">>>"'
   Python-specific usage examples; begun with ">>>"
   >>> print '(cut and pasted from interactive Python sessions)'
   (cut and pasted from interactive Python sessions)


10.6 Two syntaxes for tables:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   1.Grid tables; complete, but complex and verbose:

   +------------------------+------------+----------+
   | Header row, column 1   | Header 2   | Header 3 |
   +========================+============+==========+
   | body row 1, column 1   | column 2   | column 3 |
   +------------------------+------------+----------+
   | body row 2             | Cells may span        |
   +------------------------+-----------------------+

   2.Simple tables; easy and compact, but limited:

   ====================  ==========  ==========
   Header row, column 1  Header 2    Header 3
   ====================  ==========  ==========
   body row 1, column 1  column 2    column 3
   body row 2            Cells may span columns
   ====================  ======================

10.7 Explicit markup blocks 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

all begin with an explicit block marker, two periods and a space:

   - Footnotes:

      .. [1] A footnote contains body elements, consistently
         indented by at least 3 spaces.
   
   - Citations:

      .. [CIT2002] Just like a footnote, except the label is
         textual.
   
   - Hyperlink targets:

      .. _Python: http://www.python.org

      .. _example:

      The "_example" target above points to this paragraph.
   
   - Directives:

      ``.. image:: mylogo.png``
   
   - Substitution definitions:

      ``.. |symbol here| image:: symbol.png``
   
   - Comments:

      .. Comments begin with two dots and a space.  Anything may
         follow, except for the syntax of footnotes/citations,
         hyperlink targets, directives, or substitution definitions.


10.8 Quoted Literal Blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   John Doe wrote::

   >> Great idea!
   >
   > Why didn't I think of that?

   You just did!  ;-)

Syntax diagram:

10.9 Line Blocks
~~~~~~~~~~~~~~~~~~

Doctree elements: line_block, line. (New in Docutils 0.3.5.)

Line blocks are useful for address blocks, verse (poetry, song lyrics), and unadorned lists, where the structure of lines is significant. Line blocks are groups of lines beginning with vertical bar ("|") prefixes. Each vertical bar prefix indicates a new line, so line breaks are preserved. Initial indents are also significant, resulting in a nested structure. Inline markup is supported. Continuation lines are wrapped portions of long lines; they begin with a space in place of the vertical bar. The left edge of a continuation line must be indented, but need not be aligned with the left edge of the text above it. A line block ends with a blank line.

This example illustrates continuation lines:

   | Lend us a couple of bob till Thursday.
   | I'm absolutely skint.
   | But I'm expecting a postal order and I can pay you back
   as soon as it comes.
   | Love, Ewan.

This example illustrates the nesting of line blocks, indicated by the initial indentation of new lines:

   Take it away, Eric the Orchestra Leader!

      | A one, two, a one two three four
      |
      | Half a bee, philosophically,
      |     must, *ipso facto*, half not be.
      | But half the bee has got to be,
      |     *vis a vis* its entity.  D'you see?
      |
      | But can a bee be said to be
      |     or not to be an entire bee,
      |         when half the bee is not a bee,
      |             due to some ancient injury?
      |
      | Singing...

Syntax diagram:

.. +------+-----------------------+
.. | "| " | line                  |
.. +------| continuation line     |
..        +-----------------------+




10.10 Block Quotes
~~~~~~~~~~~~~~~~~~~~

Doctree element: block_quote, attribution.

A text block that is indented relative to the preceding text, without preceding markup indicating it to be a literal block or other content, is a block quote. All markup processing (for body elements and inline markup) continues within the block quote:

   This is an ordinary paragraph, introducing a block quote.

      "It is my business to know things.  That is my trade."

      -- Sherlock Holmes

A block quote may end with an attribution: a text block beginning with "--", "---", or a true em-dash, flush left within the block quote. If the attribution consists of multiple lines, the left edges of the second and subsequent lines must align.

Multiple block quotes may occur consecutively if terminated with attributions.

   Unindented paragraph.

      Block quote 1.

                                                         -—Attribution 1

      Block quote 2.

Empty comments may be used to explicitly terminate preceding constructs that would otherwise consume a block quote:

   * List item.

   ..

      Block quote 3.
   
Empty comments may also be used to separate block quotes:

      Block quote 4.

   ..

      Block quote 5.

Blank lines are required before and after a block quote, but these blank lines are not included as part of the block quote.

Syntax diagram:


+------------------------------+
| (current level of            |
| indentation)                 |
+------------------------------+
   +---------------------------+
   | block quote               |
   | (body elements)+          |
   |                           |
   | -- attribution text       |
   |    (optional)             |
   +---------------------------+

