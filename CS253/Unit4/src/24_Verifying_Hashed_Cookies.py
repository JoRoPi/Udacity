# -*- coding: utf-8 -*-
import hashlib

def hash_str(s):
    return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))

# -----------------
# User Instructions
# 
# Implement the function check_secure_val, which takes a string of the format 
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None 

def check_secure_val(h):
#    h_split = h.split(',')
#    if len(h_split) == 2:
#        if hash_str(h_split[0]) == h_split[1]:
#            return  h_split[0]
    # Otra solución mejor
    val = h.split(',')[0]
    if h == make_secure_val(val):
        return val

print check_secure_val('JoRoPi,654a012a11c343753c22aa760fae6a0e')
print check_secure_val('JoRoPi')
print check_secure_val('')
print check_secure_val(',')




