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

#Запрос GET
def get_habrahabr():
    response = urllib2.urlopen('http://habrahabr.ru/')
    print(response.code)
    print(response.info())  #Это header
    html = response.read()  #Это body
    response.close()

    print(html)

#Запрс POST
def find_pet_by_tag(ta):
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    query_args = {'tags': tag}
    data = urllib.urlencode(query_args)
    full_url = '{}?{}'.format(url, data)
    print(full_url)

    request = urllib2.Request(full_url, headers={
        'Accept': 'application/json'
        #   'Accept': 'application/xml'
        })
    response = urllib2.urlopen(request)
    print(response.info())
    print(response.read())
    response.close()

if __name__ == '__main__':
    #get_habrahabr()
    find_pet_by_tag('string')