# -*- coding: utf-8 -*-
from flask import Flask
from flask import Blueprint

# 定义一个蓝图 , 其实也就是一个模块 ...
btest = Blueprint("best", __name__)


@btest.route("/")
def test_model():
    return "test_model"
