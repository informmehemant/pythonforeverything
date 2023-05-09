'''
Definations singleton functions

'''


class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


my_singleton = Singleton()
another_singleton = Singleton()
print(my_singleton is another_singleton)
