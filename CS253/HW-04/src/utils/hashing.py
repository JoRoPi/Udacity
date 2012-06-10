# -*- coding: utf-8 -*-

import lib.erlichmen_py_bcrypt_8fc098d.bcrypt as bcrypt
import hmac


SECRET = '1xDjdO47nuQpRyeRGUUecfOq0ywJ2v'
def _hash_str(s):
    ###Your code here
    return hmac.new(SECRET, s).hexdigest()

def make_cookie_hash(cookie):
    return "%s|%s" % (cookie, _hash_str(cookie))

# Versión basada en bcrypt, pero lo que hago mal es que envío el salt en la cookie, habría que guardarlo en otro sitio
#def make_cookie_hash(cookie, salt=None):
#    if not salt:
#        salt = bcrypt.gensalt(2)
#    cookie_hashed = bcrypt.hashpw(cookie, salt)
#    return '%s|%s|%s' % (cookie, cookie_hashed, salt)

def get_cookie(cookie_hashed):
    val = cookie_hashed.split('|')[0]
    if cookie_hashed == make_cookie_hash(val):
        return val


# Versión basada en bcrypt, pero lo que hago mal es que envío el salt en la cookie, habría que guardarlo en otro sitio
#def get_cookie(cookie_hashed):
#    parts = cookie_hashed.split('|')
#    if len(parts) == 3:
#        if cookie_hashed == make_cookie_hash(parts[0], parts[2]):
#            return parts[0]

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = bcrypt.gensalt(2)
    pw_hashed = bcrypt.hashpw(name + pw, salt)
    return '%s|%s' % (pw_hashed, salt)

def valid_pw(name, pw, h):
    return h == make_pw_hash(name, pw, h.split('|')[1])

