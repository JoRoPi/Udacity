# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.
import string

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    base = 1
    ret = ''
    for c in reversed(word):
        if c in string.ascii_uppercase:
            ret += str(base) + '*' + c + '+'
            base *= 10
        else:
            ret += c
    if word[-1] != '+':
        if ret[-1] == '+':
            ret = ret[:-1]
    return ret

def compile_word2(word):
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

print compile_word('YOU')
print compile_word('+')
print compile_word2('YOU')
print compile_word2('+')
word = 'YOU'
print word
print word[::-1]
for (i, d) in enumerate(word[::-1]) : print i, d
