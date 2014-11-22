# -*- coding: utf-8 -*-
"""
Wkhtmltopdf python wrapper to convert html to pdf using the webkit rendering engine and qt
"""

__author__ = 'Golovanov Stanislav'
r_version__ = '0.5.0'
__license__ = 'MIT'

from .pdfkit import PDFKit
from .api import from_url, from_file, from_string, configuration
