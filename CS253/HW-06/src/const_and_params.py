# -*- coding: utf-8 -*-

_page_home = '/blog'
_page_new_post = _page_home + '/newpost'
_page_signup = _page_home + '/signup'
_page_welcome = _page_home + '/welcome'
_page_login = _page_home + '/login'
_page_logout = _page_home + '/logout'
_page_home_json = _page_home + '/.json'
_page_flush_cache = _page_home + '/flush'

def get_page_home():
    return _page_home

def get_page_new_post():
    return _page_new_post

def get_filter_post_permalink_json():
    return _page_home + '/([0-9]+).json'

def get_filter_post_permalink():
    return _page_home + '/([0-9]+)'

def get_page_signup():
    return _page_signup

def get_page_welcome():
    return _page_welcome

def get_page_login():
    return _page_login

def get_page_logout():
    return _page_logout

def get_page_home_json():
    return _page_home_json

def get_page_flush_cache():
    return _page_flush_cache
