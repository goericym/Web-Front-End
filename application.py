# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

from a import btest

application = Flask(__name__)

# 注册蓝图 test_model ,
# 蓝图的作用是吧路由放到更多的文件中去 ,
# 避免一个文件中的路由 太多而难以维护
# 此时访问localhost/blueprint/blueprint 即访问了a.py文件中的test_model 路由模块

application.register_blueprint(btest, url_prefix='/blueprint')


@application.route('/')
def function():
     return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True)
