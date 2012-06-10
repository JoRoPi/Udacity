import string

table = string.maketrans('ABC', '123')
f = 'A + B == C'
print f
t = f.translate(table)
print t
print eval(t)

