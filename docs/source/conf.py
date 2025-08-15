# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ARC Software Guide'
copyright = u'2021–%Y — The University of Oxford'
author = 'The ARC Team'

release = ''
version = ''

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    "sphinx_favicon",
    "sphinx_rtd_dark_mode",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

pygments_style = 'sphinx'

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_favicon = 'favicon.ico'
html_theme_options = {
    'version_selector': False,
    'language_selector': False,
}

# user starts in light mode
default_dark_mode = False

# -- ARC Customisations

html_logo = 'images/arc_logo-wide-white.svg'

# -- Add ARC theme overrides...
# This will be found in source/_static (as defined above)
html_static_path = ['_static']
html_css_files = [
    'css/arc_theme.css',
]
favicons = [
    {"href": "arc_icon.svg"},
    {"href": "favicon16.png"},
    {"href": "favicon32.png"},
    {"href": "favicon96.png"},
    {"href": "favicon160.png"},
]

#html_show_copyright = False
html_show_sphinx = False

# -- Options for EPUB output
epub_show_urls = 'footnote'
