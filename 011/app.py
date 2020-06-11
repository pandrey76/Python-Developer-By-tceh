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

from backline.rest.api import views

app = _CustomFlask('backline')
app.config.update(**settings.as_dict())
app.debug = settings.DEBUG  #not always set
app.register_blueprint(views)

app.route('/healthcheck')
def healthcheck():
    """
    """
if __name__ == '__main__':
    main()
