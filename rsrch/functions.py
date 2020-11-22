import hashlib

import pdfkit

from rsrch.settings.base import (
    PDF_BASE_TEMPLATE, PDF_OPTIONS, PDF_RESULTS_DIR
)
from rsrch.settings.productive import SITE_HOST


class Context(dict):
    def __missing__(self, key):
        return f'{key}'


def make_pdf(content, filename):
    if not PDF_RESULTS_DIR.is_dir():
        PDF_RESULTS_DIR.mkdir()
    pdfkit.from_string(content, PDF_RESULTS_DIR / f'{filename}.pdf', options=PDF_OPTIONS)


def fill_template(template, data):
    context = Context(**data)
    return template.format_map(context)


def get_pdf_content(document_template, data, ending_page_url):
    filled_document = fill_template(template=document_template, data=data)
    return PDF_BASE_TEMPLATE.format(content=filled_document, ending_page=f'{SITE_HOST}{ending_page_url}')


def str_m5(string, encoding='utf8'):
    if not isinstance(string, str):
        string = str(string)
    return hashlib.md5(string.encode(encoding)).hexdigest()
