# -*- coding: utf-8 -*-

#class ConstAndParam:
_home_page = '/blog'
_new_post_page = _home_page + '/newpost'

def get_home_page():
    return _home_page

def get_new_post_page():
    return _new_post_page

def get_post_permalink_filter():
    return _home_page + '/([0-9]+)'
