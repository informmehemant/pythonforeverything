'''
Pattern name - SingleTon(Mono state pattern)
Pattern type - creational Design Pattern

this is called Borg solutions


'''

# Solution - 1

class Borg(object):
    # class variable this is global
    _shared = {}
#    shared the whole state of Object 
    def __init__(self):
        self.__dict__ = self._shared

class SingleTon(Borg):
    # Borg is the parent class
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

o1 = SingleTon("Hardik")
print("Object - 1 ==> ", o1)
print("Object - 1 val ==>", o1.val)


o2 = SingleTon("Shashi")
print("Object - 2 ==> ", o2)
print("Object - 2 val ==>", o2.val)

print("Object - 1 val ==>", o1.val )
'''
conclusion 
o1,o2 are different object still sharing the same state
even addr is different still sharing the same state
example below
'''

print( o1.__dict__)
print( o2.__dict__)




        