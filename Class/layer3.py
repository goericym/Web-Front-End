from flask import Blueprint
from flask import g
from flask import render_template

layer3_bp = Blueprint('layer3', __name__,
                      url_prefix='/<layer1>/<layer2>/<layer3>')


@layer3_bp.url_value_preprocessor
def get_lang_code_from_url(endpoint, view_args):
    g.layer3 = view_args.pop('layer3')


@layer3_bp.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('layer3', g.layer3)


@layer3_bp.route('/')
def index(layer1, layer2):
    index_url = layer1 + '/' + layer2 + '/' + g.layer3 + '/index.html'
    return render_template(index_url)
