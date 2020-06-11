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


@app.route('/', methods=['GET', 'POST'])
def home():
    print(request)
    return 'hello world!', 200

#print(request, type(request), request.method)

with app.test_request_context('/next=http://example.com'):
    print(request, type(request), request.method)


if __name__ == '__main__':
    app.run()
