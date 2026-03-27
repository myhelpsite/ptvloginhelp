project = 'Peacock TV'
author = 'Peacock TV`'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Google & Bing Verification Meta Tags
html_context = {
    "meta_tags": """
    <meta name="google-site-verification" content="vWuKdfn7mBaw-KlLRh8j_GtlIs4FQ-h0VcG-WO8D8ns" />
  <meta name="msvalidate.01" content="649552A7F8FC8C674CD07172F20F2D02" />
    """
}
