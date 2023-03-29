'''
Pattern name - SingleTon
Pattern type - Creational Design Pattern
'''
'''
some example using __call__ method
'''
class Test:
    
    def __init__(self):
        self.x = 2
    def __call__(self, y):
        return self.x + y
    
call = Test()

print(call(3))

        
# Solution - 3
class SingleTonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance
    

@SingleTonDecorator
class Logger:
    def __init__(self):
        self.start = None
    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)


logger1 = Logger()
logger1.start = "# >"
print("Logger 1", logger1)
logger1.write("Logger1 object is created.")

logger2 = Logger()
logger2.start = "$ >"
print("Logger 2", logger2)
logger1.write("Logger2 object is created.")



