# This Python file uses the following encoding: utf-8
class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        """An other comment"""
        return 'hello world'
    
    def __init__(self):
        """This is the class init method, similar to a constructor"""
        self.data = []

print MyClass.i
print MyClass.f
print MyClass.__doc__
print MyClass.f.__doc__

x = MyClass()

print x.i
print x.f
print x.__doc__
print x.f.__doc__

print x.data

# Añadimos por la cara un atributo, data attribute, a la instancia que al final eliminamos.
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print x.counter
del x.counter
print x.__class__

class BaseClass(object):
    def __init__(self):
        print "This is the BaseClass"

class DeriveClass(BaseClass):
    def __init__(self):
        #BaseClass.__init__(self)
        super(BaseClass,self).__init__()
        print "This is the DeriveClass"

y = DeriveClass()
print y.__class__
print type(y)

