#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     09.04.2018
# Copyright:   (c) Prapor 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask, request


app = Flask(__name__)


#По хорошему функция home должна получить request, а вернуть response, во
#всяком случае так делается во всех нормальных фрэймворках (Django например)
@app.route('/', methods=['GET', 'POST'])
def home():
    print(request)
    return 'hello world!', 200

# Единственное для чего нужен объект request – это только получение данных
#от пользователя. Это то место где хранится информация о нашем запросе.

#Вне route работать с request скорей всего не придётся, если нам зачем то это
#всё таки надо будет сделать, то скорей всего мы делаем что то неправильно.
#Ну в принципе это можно сделать через менаджер контекста например так:
with app.test_request_context('/next=http://example.com'):
    print(request, type(request), request.method)


if __name__ == '__main__':
    app.run()
