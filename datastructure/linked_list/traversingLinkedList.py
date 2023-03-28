
# Node creations
'''
creation of node which has data_value and next_value

'''

class Node:
    def __init__(self, data_value) -> None:
        self.data_value = data_value
        self.next_value = None


'''
head creation(head_value) needs to get pointed with data_value
'''

class SLinkedList:
    def __init__(self) -> None:
        self.head_value = None

    def print(self):
        while self.head_value is not None:
            print()


