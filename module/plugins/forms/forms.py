#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (C) 2009-2012:
#    Gabes Jean, naparuba@gmail.com
#    Gerhard Lausser, Gerhard.Lausser@consol.de
#    Gregory Starck, g.starck@gmail.com
#    Hartmut Goebel, h.goebel@goebel-consult.de
#
# This file is part of Shinken.
#
# Shinken is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Shinken is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Shinken.  If not, see <http://www.gnu.org/licenses/>.


### Will be populated by the UI with it's own value
app = None


def form_submit_check(name):
    user = app.check_user_authentication()

    t = 'host'
    if '/' in name:
        t = 'service'

    return {'app': app, 'user': user, 'name': name, 'obj_type': t}


def form_change_var(name):
    user = app.check_user_authentication()

    variable = app.request.GET.get('variable', '')
    value = app.request.GET.get('value', '')
    
    if '/' in name:
        elt = app.get_service(name.split('/')[0], name.split('/')[1])
    else:
        elt = app.get_host(name)

    return {'app': app, 'user': user, 'elt': elt, 'name': name, 'variable': variable, 'value': value}

def form_var(name):
    user = app.check_user_authentication()

    if '/' in name:
        elt = app.get_service(name)
    else:
        elt = app.get_host(name)

    return {'app': app, 'user': user, 'elt': elt, 'name': name}

def form_ack_add(name):
    user = app.check_user_authentication()
    return {'app': app, 'user': user, 'name': name}
def form_ack_remove(name):
    user = app.check_user_authentication()
    return {'app': app, 'user': user, 'name': name}

def form_comment_add(name):
    user = app.check_user_authentication()
    return {'app': app, 'user': user, 'name': name}
def form_comment_delete(name):
    comment = app.request.GET.get('comment', '-1')
    user = app.check_user_authentication()
    return {'app': app, 'user': user, 'name': name, 'comment': comment}
def form_comment_delete_all(name):
    user = app.check_user_authentication()
    return {'app': app, 'user': user, 'name': name}

def form_downtime_add(name):
    user = app.check_user_authentication()
    return {'app': app, 'user': user, 'name': name}
def form_downtime_delete(name):
    user = app.check_user_authentication()
    downtime = app.request.GET.get('downtime', '-1')
    return {'app': app, 'user': user, 'name': name, 'downtime': downtime}
def form_downtime_delete_all(name):
    user = app.check_user_authentication()
    return {'app': app, 'user': user, 'name': name}


pages = {
        form_submit_check:          {'routes': ['/forms/submit_check/<name:path>'],             'view': 'form_submit_check'},
        
        form_change_var:            {'routes': ['/forms/change_var/<name:path>'],               'view': 'form_change_var'},
        
        form_comment_add:           {'routes': ['/forms/comment/add/<name:path>'],              'view': 'form_comment_add'},
        form_comment_delete:        {'routes': ['/forms/comment/delete/<name:path>'],           'view': 'form_comment_delete'},
        form_comment_delete_all:    {'routes': ['/forms/comment/delete_all/<name:path>'],       'view': 'form_comment_delete_all'},
        
        form_downtime_add:          {'routes': ['/forms/downtime/add/<name:path>'],             'view': 'form_downtime_add'},
        form_downtime_delete:       {'routes': ['/forms/downtime/delete/<name:path>'],          'view': 'form_downtime_delete'},
        form_downtime_delete_all:   {'routes': ['/forms/downtime/delete_all/<name:path>'],      'view': 'form_downtime_delete_all'},
        
        form_ack_add:               {'routes': ['/forms/acknowledge/add/<name:path>'],          'view': 'form_ack_add'},
        form_ack_remove:            {'routes': ['/forms/acknowledge/remove/<name:path>'],       'view': 'form_ack_remove'},
        }
