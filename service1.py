# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template

# 定義一個blueprint,其實也就是一個模塊
btest = Blueprint("service1", __name__, url_prefix='/en/service1')


@btest.route("/")
def test_model():
    return render_template('en/index.html')
