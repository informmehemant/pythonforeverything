'''
Pattern name - SingleTon
Pattern type - Creational Design Pattern

'''

# Solution - 3

class SingleTonDecorator(object):
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args,**kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance
    

@SingleTonDecorator
class Logger(object):
    def __init__(self):
        self.start = None
    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)
        

