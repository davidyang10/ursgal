#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
#
# ursgal documentation build configuration file, created by
# sphinx-quickstart on Mon Sep 14 09:56:34 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex
from collections import defaultdict as ddict
import pprint
import glob
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../../tests/'))
sys.path.insert(0, os.path.abspath('../../example_scripts/'))
sys.path.insert(0, os.path.abspath('../../'))
from ursgal.uparams import ursgal_params

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    # 'sphinxcontrib.exceltable',
    # 'sphinx.ext.viewcode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'ursgal'
copyright = '2015, Lukas P. M. Kremer, Purevdulam Oyunchimeg, Johannes Barth, Stefan Schulze and Christian Fufezan'
author = 'Lukas P. M. Kremer, Purevdulam Oyunchimeg, Johannes Barth, Stefan Schulze and Christian Fufezan'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# We store our version number in a simple text file:
version_path = os.path.join(
    os.path.dirname(__file__),
    os.pardir, os.pardir,
    'ursgal', 'version.py'
)
with open(version_path, 'r') as version_file:
    ursgal_version = version_file.read().strip()

# The short X.Y version.
version = ursgal_version
# The full version, including alpha/beta/rc tags.
release = ursgal_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme = 'default'
else:
    # html_theme = 'default'
    html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'ursgaldoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'ursgal.tex', 'ursgal Documentation',
   'Lukas P. M. Kremer,\\\\Purevdulam Oyunchimeg,\\\\Johannes Barth,\\\\Stefan Schulze and\\\\Christian Fufezan', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ursgal', 'ursgal Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'ursgal', 'ursgal Documentation',
   author, 'ursgal', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


_table_headers = ['style', 'translation', 'translated value', 'ursgal value']

minimal_width = max([ len(t) for t in _table_headers])

PARAMS_FILE = open('parameter.txt', 'w')

def create_format_string( number_of_columns = 1 ):
    fmt = ''
    for n in range(number_of_columns):
        fmt += ' {' + str(n) + ': <{width}}'
    return fmt


def determine_longest_string( fdict ):
    len_longest = minimal_width
    for k, value in fdict.items():
        if isinstance(k, bool):
            k = 'False'
        # print(k,value)
        if len(str(k)) > len_longest:
            len_longest = len(k)
        if isinstance(value, dict):
            # value translations
            len_in_nested = determine_longest_string( value)
            if len_in_nested > len_longest:
                len_longest = len_in_nested
        elif isinstance(value, bool):
            pass
        elif value is None:
            pass
        elif isinstance(value, float):
            pass
        elif isinstance(value, int):
            pass
        elif isinstance(value, tuple):
            pass
        else:
            if len(value) > len_longest:
                len_longest = len(value)
    return len_longest


def uprint( string ):
    print( string, file = PARAMS_FILE)
    # print( string )
    return

def print_error( udict, syntax_error_at='unkown' ):
    pprint.pprint( udict )
    print('Syntax error @ {0}'.format( syntax_error_at ))


print(
    'Converting ursgal.uparams to sphinx. [ source/parameter.txt ] '
)
uprint('''
.. _parameters:

Ursgal Parameters
*****************

A Dash script has been built in order to make it easier to explore uparams.
It allows for searching for specific uparams, filtering by UNodes (i.e. engines),
and filtering by utags.
To install Dash, follow the instructions on
    | https://dash.plot.ly/

Afterwards, just go to the docs folder and execute the script::

    user@localhost:~/ursgal/docs$ python3.4 uparams_to_dash.py

A local server will be created and view the interactive page:
    | http://127.0.0.1:8050/

Besides this, all uparams are still listed here as part of the documentation.


.. note:: This sphinx source file was **auto-generated** using
    ursgal/docs/uparams_to_sphinx_docu.py, which parses ursgal/ursgal/uparams.py
    Please **do not** modify this file directly, but commit changes to ursgal.uparams.


''')
for ursgal_param, udict in sorted(ursgal_params.items()):
    # if len(udict['available_in_unode']) <= 5:
    #     continue
    if isinstance(udict['default_value'], dict):
        default_value = str(sorted(udict['default_value'])).strip()
    else:
        default_value = str(udict['default_value']).strip()
    uprint('''
.. raw:: html

  <hr />

{0}
{1}


{desc}

:Default value: {default_value}
:type: {type}
:triggers rerun: {rerun}
        '''.format(
        ursgal_param,
        '#' * (len(ursgal_param) + 11),
        desc = udict['description'].strip(),
        default_value = default_value,
        type = udict.get('uvalue_type', ''),
        rerun = udict.get('triggers_rerun', 'False')
    ))

    uprint('''
Available in unodes
"""""""""""""""""""
''')
    for unode in udict['available_in_unode']:
        uprint('* {0}'.format( unode ))
    uprint('''
Ursgal key translations for *{0}*
""""""""""""""""""""""""""""""{1}
'''.format( ursgal_param, '"'*len(ursgal_param)))
    len_longest = determine_longest_string( udict['ukey_translation']  )
    fmt = create_format_string( number_of_columns = 2 )
    delimiter_text = ['=' * len_longest ] * 2
    try:
        uprint( fmt.format(*delimiter_text, width=len_longest))
    except:
        print( delimiter_text )
        print( udict['ukey_translation'])
        exit(1)
    uprint( fmt.format('Style', 'Translation', width=len_longest))
    uprint( fmt.format(*delimiter_text, width=len_longest))
    for style, translation in sorted(udict['ukey_translation'].items()):
        try:
            uprint( fmt.format(style, '{0}'.format(translation), width=len_longest))
        except:
            print( fmt , style, translation, len_longest )
            exit(1)
    uprint( fmt.format(*delimiter_text, width=len_longest))

    if len( udict['uvalue_translation'] ) == 0:
        continue
    uprint('''
Ursgal value translations
"""""""""""""""""""""""""
''')
    len_longest = determine_longest_string( udict['uvalue_translation']  )
    fmt = create_format_string(
        number_of_columns =  len(udict['uvalue_translation'].keys()) + 1
    )
    nmbr_of_val_translations = len(udict['uvalue_translation'].keys())
    delimiter_text = ['=' * len_longest ] * ( nmbr_of_val_translations + 1)
    header_text_1 = [
        '{0: <{1}}'.format('Ursgal Value', len_longest),
        '{0: <{1}}'.format('Translated Value', len_longest),
    ] + [''] * (nmbr_of_val_translations - 1)

    header_text_2 = [
        '{0: >{1}}'.format('-' * (len_longest), len_longest),
        '{0}'.format(
            '-'.join(
                ['-' * len_longest] * len(udict['uvalue_translation'].keys())
            )
        ),
    ] + [''] * (nmbr_of_val_translations )
    header_text_3 = ['{0: <{1}}'.format('.', len_longest)]
    row_predicts = {}
    for style, fdict in sorted(udict['uvalue_translation'].items()):
        header_text_3.append(
            '{0: <{1}}'.format(style, len_longest),
        )
        try:
            for uvalue_unformated, translated_value in sorted(fdict.items()):
                # header_text_3.append( '{0: <{1}}'.format(uvalue_unformated, len_longest) )
                if translated_value is None:
                    translated_value = 'None'
                uvalue = '{0: <{1}}'.format(uvalue_unformated, len_longest)
                if uvalue not in row_predicts.keys():
                    row_predicts[ uvalue ] = {
                        s : 'n/t' for s in udict['uvalue_translation'].keys()
                    }
                row_predicts[ uvalue ][ style ] = '{0: <{1}}'.format(
                    translated_value, len_longest
                )
        except:
            print(fdict)
            print_error( udict, syntax_error_at = 'uvalue_translation' )
            # for uvalue_unformated, translated_value in sorted(fdict.items()):
            #     # header_text_3.append( '{0: <{1}}'.format(uvalue_unformated, len_longest) )
            #     uvalue = '{0: <{1}}'.format(uvalue_unformated, len_longest)
            #     if uvalue not in row_predicts.keys():
            #         row_predicts[ uvalue ] = {
            #             s : 'n/t' for s in udict['uvalue_translation'].keys()
            #         }
            #     row_predicts[ uvalue ][ style ] = '{0: <{1}}'.format(
            #         translated_value, len_longest
            #     )
            exit(1)
    uprint( fmt.format(*delimiter_text, width=len_longest))
    uprint( fmt.format(*header_text_1, width=len_longest))
    uprint( fmt.format(*header_text_2, width=len_longest).rstrip())
    uprint( fmt.format(*header_text_3, width=len_longest))
    uprint( fmt.format(*delimiter_text, width=len_longest))

    for uvalue, fdict in sorted( row_predicts.items() ):
        row = [ uvalue ]
        for k, v in sorted(fdict.items()):
            row.append( v )
        uprint( fmt.format(*row, width=len_longest))
    uprint( fmt.format(*delimiter_text, width=len_longest))
uprint('''

.. params ending on _ are links ... one can escape them with \_ but well well

.. _score:
   http://http://www.uni-muenster.de/Biologie.IBBP.AGFufezan/

.. _proteinacc_start_stop_pre_post:
    http://http://www.uni-muenster.de/Biologie.IBBP.AGFufezan/

.. _decoy:
    http://http://www.uni-muenster.de/Biologie.IBBP.AGFufezan/

    ''')

#
# Example script parsing
#
print('''
    Formatting example scripts into rst files for the docs
''')
# input()
for example_script in glob.glob('../../example_scripts/*.py'):
    if os.path.exists(example_script) is False:
        continue
    basename= os.path.basename(example_script)
    print('Reading: {0}'.format(example_script))
    with open('code_inc/{0}'.format(basename.replace('.py','.inc')), 'w') as o:
        print('''.. code-block:: python\n''', file=o)
        with open( example_script ) as infile:
            for line in infile:
                print('\t{0}'.format( line.rstrip()), file=o)

