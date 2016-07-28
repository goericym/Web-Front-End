from flask import Blueprint
from flask import g
from flask import render_template

layer2_bp = Blueprint('layer2', __name__, url_prefix='/<layer1>/<layer2>')


@layer2_bp.url_value_preprocessor
def get_lang_code_from_url(endpoint, view_args):
    g.layer2 = view_args.pop('layer2')


@layer2_bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('layer2', g.layer2)


@layer2_bp.route('/')
def index(layer1):
    index_url = layer1 + '/' + g.layer2 + '/index.html'
    return render_template(index_url)


@layer2_bp.route('/<page>')
def page(layer1, page):
    index_url = layer1 + '/' + g.layer2 + '/' + page + '.html'
    return render_template(index_url)
