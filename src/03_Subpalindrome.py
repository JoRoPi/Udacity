import json
from string import find

class RecString(str):
    def __init__(self, text):
        self.steps = [text]
        self.index = 0
    
    def __eq__(self, other):
        if other is '':
            return not len(self)
        
        if len(self) != 1 or len(other) != 1 or not isinstance(other, RecString):
            self.error()
        
        equal = str.__eq__(self, other)
        self.steps.append(['c', self.index, other.index, 1 if equal else 0])
        return equal
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __getitem__(self, *args):
        if (len(args) > 1):
            self.error()
        else:
            return self.baby(str.__getitem__(self, *args), args[0])
            
    def __getslice__(self, *args):
        self.error()
        
    def lower(self):
        return self.baby(str.lower(self), self.index)
        
    def upper(self):
        return self.baby(str.upper(self), self.index)
    
    def baby(self, text, index):
        baby = RecString(text)
        baby.steps = self.steps
        baby.index = index
        return baby
    
    def error(self):
        raise Exception("""
        Please access only individual characters: e.g. text[a]
        Comparisons such as text == text[::-1] are O(n),
        do them explicitly one character at a time.
        """)
    
    def get_recording_link(self):
        return ('http://explored.tk/experiments/palindrome#[%s]' %
                json.dumps(self.steps, separators=(',',':')))

# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    i = j = current = 0
    final = -1
    l = len(text)

    def test_palim(i, j):
        if i == j: return True
        if j < i: return True
        return text[i] == text[j] and test_palim(i+1, j-1) 
    
    if l > 1:
        text = text.lower()
        j_less_i = j-i
        while l-current > j_less_i:
            if final == -1: final = l
            final = text.rfind(text[current], current+1, final)
            if final == -1:
                current += 1
            else:
                if final-current > j_less_i:
                    if not test_palim(current+1, final-1):
                        # tray again with update final
                        continue
                    else:
                        if final-current > j_less_i:
                            i = current
                            j = final+1
                            j_less_i = final-i
                current +=1
                final = l

    return (i,j)


    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
text = RecString('123454311123454321010')
#text = RecString('racecar')
#text = RecString('Racecar')
#text = RecString('RacecarX')
#text = RecString('Race carr')
#text = RecString('')
#text = RecString('something rac e car going')
#text = RecString('xxxxx')
#text = RecString('Mad am I ma dam.')
print longest_subpalindrome_slice(text)
print text.get_recording_link()

