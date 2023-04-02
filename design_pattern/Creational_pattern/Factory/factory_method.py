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
        pass
    def addDegree(self, degree):
        self._degrees.append(degree)

    def getDegrees(self):
        return self._degrees
class ManageFactory(ProfileAbstractFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(ME())
class ProfileCreatorFactory(object):
    @classmethod
    def create_profile(self, name):
        return eval(profile_type + 'Factory')()
    
if __name__ == '__main__':
    profile_type = input("Which Profile woulf you like to create? Manger/Engineer- ")
    profile = ProfileCreatorFactory.create_profile(profile_type)
    print("Create Profile of ",profile_type)
    print("Profile has following degrees -")
    for deg in profile.getDegrees():
        print('- ', deg)