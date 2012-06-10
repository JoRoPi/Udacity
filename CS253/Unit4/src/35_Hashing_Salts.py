import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# implement the function make_pw_hash(name, pw) that returns a hashed password 
# of the format: 
# HASH(name + pw + salt),salt
# use sha256

def make_pw_hash(name, pw):
    salt = make_salt()
    return '%s,%s' % (hashlib.sha256(name + pw + salt).hexdigest(), salt)

print make_pw_hash('JoRoPi', '12345')