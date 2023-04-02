class SingletonMeta(type):
    '''
    The SingleTon class can be implemented in different ways in python. Some 
    possible methods includes: base class, decorator, metaclass. We will use the metaclass because it is best suited for this purpose.

    '''

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args,**kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
'''
In this code snippet, cls refers to the class that defines the __call__ method. The line if cls not in cls._instances: checks if the class has already been instantiated and stored in the _instances dictionary.

The _instances dictionary is a class-level variable that keeps track of all the instances of the class that have been created so far. It is a common technique used in the Singleton design pattern to ensure that only one instance of the class is created and reused across the application.

If the class has not been instantiated before, the __call__ method creates a new instance of the class by calling the super().__call__(*args, **kwargs) method. This method invokes the class's constructor with the provided arguments and returns a new instance of the class.

Finally, the __call__ method adds the newly created instance to the _instances dictionary and returns it. If the class has already been instantiated before, the method simply returns the existing instance from the _instances dictionary, instead of creating a new instance.

Overall, the if cls not in cls._instances condition checks if a new instance of the class needs to be created or if an existing instance can be reused.

'''
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        '''
        Finally, any singleton should define some business logic, which can be executed on its instance.
        '''


if __name__ == "__main__":
    # the client code .
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variable contain the same instance.")
    else:
        print("Songleton fails, variable contain different instance.")



