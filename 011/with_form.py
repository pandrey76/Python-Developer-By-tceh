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

#pip install flask-WTF
from flask_wtf import FlaskForm
from wtfform import StringField, validators

class ContactForm(FlaskForm):
    name = StringField(validators=[
         validators.Length(min=4, max=25)    # NIKITA
                    ])

    email = StringField(validators=[
         validators.Length(min=6, max=35),
         validators.Email() # mail@sobolev.me
                    ])

    job = StringField(validators=[])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    #SECRET_KEY=os.environ['S'],
    WTF_CSRF_ENABLED=False, #очень важный флаг, необходим для работы с Postman,
                            #сервер при данном флаге не делает очень много
                            #проверок в части безопасности при "Post" запросах.
)

#Ещё один вариант инициализации настроек
#app.config['DEBUG'] = True
#app.config['SECRET_KEY'] = os.environ['S']


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())
    return 'hello world!', 200

#print(request, type(request), request.method)

with app.test_request_context('/'):
    print(request, type(request), request.method)


if __name__ == '__main__':
    app.run()
