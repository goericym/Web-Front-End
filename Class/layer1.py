from flask import Blueprint
from flask import g
from flask import render_template

layer1_bp = Blueprint('layer1', __name__, url_prefix='/<layer1>')


@layer1_bp.url_value_preprocessor
def get_lang_code_from_url(endpoint, view_args):
    g.layer1 = view_args.pop('layer1')


@layer1_bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('layer1', g.layer1)


@layer1_bp.route('/')
def index():
    index_url = g.layer1 + '/index.html'
    return render_template(index_url)
