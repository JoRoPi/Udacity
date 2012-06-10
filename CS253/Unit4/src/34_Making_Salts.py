import random
import string

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    return ''.join(random.choice(string.letters) for _ in xrange(5))

print string.letters
print random.choice(string.letters)
print ''.join(random.choice(string.letters) for _ in xrange(5))
print make_salt()