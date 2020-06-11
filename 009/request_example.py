#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     06.04.2018
# Copyright:   (c) Prapor 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib
import urllib2

__author__ = 'Prapor'

def get_habrahabr():
    r = request.get('http://habrahabr.ru/')
    print(r.code)
    print(r.headers)
    print(r.content)

def find_pet_by_tag(ta):

    params = {'tags': tag}
    headers={
        'Accept': 'application/xml'
    }
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    r = request.get(url, params = params, headers = headers)
    print(r.status_code, r.headers)
    print(r.content)

    #s = 'http://petstore.swagger.io/v2/pet/89?tags=string&filter=sad'


if __name__ == '__main__':
    #get_habrahabr()
    find_pet_by_tag('string')
