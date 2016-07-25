from flask import Blueprint, g, url_for

lang_bp = Blueprint('lang', __name__, url_prefix='/<lang_code>')

@lang_bp.url_value_preprocessor
def get_lang_code_from_url(endpoint, view_args):
    g.lang_code = view_args.pop('lang_code')

@lang_bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@lang_bp.route('/')
def index():
    return '<h1>Index of language %s</h1>' % g.lang_code
 
@lang_bp.route('/<path>')
def path(path):
    return '<h1>Language base URL is %s , %s</h1>' % (url_for('.index', lang_code=g.lang_code),path)
