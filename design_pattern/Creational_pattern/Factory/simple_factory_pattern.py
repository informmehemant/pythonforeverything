'''
learn how to create simple
factory which helps to hide logic of creating objects.

object creation is not dependent on Class
pen factory -> 
-> they will give u pen but will not show you how it's build
-> if you ask new type of pen then factory will cater for it 
   while creating another scections

'''

from abc import ABCMeta, abstractclassmethod

class Person(metaclass=ABCMeta):
    @abstractclassmethod
    def create(self):
        pass
class HR(Person):
    def create(self, name):
        print(f"Enginner {name} is created")

class PersonFactory(object):
    @classmethod
    def createPerson(cls,designation,name):
        #  This is python method of creating string to method 
        # in this care HR is given it call's to HR method 
        eval(designation)().create(name)


if __name__ == "__main__":
    designation = input("Please enter the designation - ")
    name = input("Please enter the person's name -")
    PersonFactory.createPerson(designation,name)