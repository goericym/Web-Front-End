# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import send_from_directory
from Class.layer1 import layer1_bp
from Class.layer2 import layer2_bp
from Class.layer3 import layer3_bp

application = Flask(__name__)

application.register_blueprint(layer1_bp)
application.register_blueprint(layer2_bp)
application.register_blueprint(layer3_bp)


@application.route('/')  # root
def index():
    return render_template('index.html')


@application.route('/static/css/<path:filename>')
def css_static(filename):
    return send_from_directory(application.root_path + '/static/css', filename)

@application.route('/static/js/<path:filename>')
def js_static(filename):
    return send_from_directory(application.root_path + '/static/js', filename)

if __name__ == '__main__':  # pragma: no cover
    application.run(debug=True)
