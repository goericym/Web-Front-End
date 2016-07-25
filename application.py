# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import g
from flask import url_for
from service1 import btest
from mod_Lang import lang_bp

application = Flask(__name__)

# register_blueprint test_model ,
# blueprint是把不同的路由 導到別的檔案裡去 ,
# 避免同一個文件中的路由 太多而難以維護
# 此时访问localhost/blueprint/ 即访问了a.py文件中的test_model 路由模块


application.register_blueprint(lang_bp)
application.register_blueprint(btest)
# @application.route('/<lang_code>/')
# def index(lang_code):
#     g.lang_code = lang_code
#     return '<h1>Index of language %s</h1>' % g.lang_code
#     # eturn render_template('tw/index.html')

# #http://127.0.0.1:5000/en/path
# @application.route('/<lang_code>/path')
# def path(lang_code):
#     g.lang_code = lang_code
# return '<h1>Language base URL is %s</h1>' % url_for('index',
# lang_code=g.lang_code)


# @application.route('/<user_id>/', defaults={'username': 'aaa'})
# @application.route('/<user_id>/<username>/')
# def show1(user_id, username):
#     aaa = user_id + username
#     return aaa
#     pass


# @application.route('/<user_id>/<username>/<abc>')
# def show(user_id, username, abc):
#     aaa = user_id + username + abc
#     return aaa
#     pass



if __name__ == '__main__':
    application.run(debug=True)
