# -*- coding: utf-8 -*-

import lib.erlichmen_py_bcrypt_8fc098d.bcrypt as bcrypt
import hmac


SECRET = '1xDjdO47nuQpRyeRGUUecfOq0ywJ2v'

def _hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_cookie_hash(cookie):
    return "%s|%s" % (cookie, _hash_str(cookie))

def get_cookie(cookie_hashed):
    val = cookie_hashed.split('|')[0]
    if cookie_hashed == make_cookie_hash(val):
        return val

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = bcrypt.gensalt(2)
    pw_hashed = bcrypt.hashpw(name + pw, salt)
    return '%s|%s' % (pw_hashed, salt)

def valid_pw(name, pw, h):
    return h == make_pw_hash(name, pw, h.split('|')[1])

