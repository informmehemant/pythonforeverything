'''

Learn how to create simple factory which helps to hide 
logic of creating objects.

'''


from abc import ABCMeta, abstractmethod

class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass

class BE(AbstractDegree):
    def info(self):
        print("Bachelor of engineering")
    def __str__(self):
        return "Bachelor of engineering"

class ME(AbstractDegree):
    def info(self):
        print("Master of engineering")
    def __str__(self):
        return "Master of engineering"

class MBA(AbstractDegree):
    def info(self):
        print("Master of business adminstration")
    def __str__(self):
        return "Master of business administration"

class ProfileAbstractFactory(object):
    def __init__(self):
        self.degrees = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        