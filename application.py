# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

from service1 import btest

application = Flask(__name__)

# register_blueprint test_model ,
# blueprint是把不同的路由 導到別的檔案裡去 ,
# 避免同一個文件中的路由 太多而難以維護
# 此时访问localhost/blueprint/ 即访问了a.py文件中的test_model 路由模块

application.register_blueprint(btest, url_prefix='/service1')


@application.route('/')
def function():
     return render_template('tw/index.html')


if __name__ == '__main__':
    application.run(debug=True)
