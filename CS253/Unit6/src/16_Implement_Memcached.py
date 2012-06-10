
# QUIZ implement the basic memcache functions

CACHE = {}

#return True after setting the data
def set(key, value):
    global CACHE
    CACHE[key] = value
    return True

#return the value for key
def get(key):
    global CACHE
    return CACHE.get(key)

#delete key from the cache
def delete(key):
    global CACHE
    if key in CACHE:
        CACHE[key] = None

#clear the entire cache
def flush():
    global CACHE
    CACHE.clear()

print set('x', 1)
#>>> True

print get('x')
#>>> 1

print get('y')
#>>> None

delete('x')
print get('x')
#>>> None