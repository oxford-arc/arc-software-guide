# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ARC Software Guide'
copyright = '2021–2024'

author = 'The ARC Team'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- ARC Customisations

html_logo = 'images/arc_logo-wide-white.svg'

# -- Add ARC theme overrides...
# This will be found in source/_static (as defined above)
html_static_path = ['_static']
html_css_files = [
    'css/arc_theme.css',
]

#html_show_copyright = False
html_show_sphinx = False
