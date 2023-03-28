class Node:
    def __init__(self, dataval=None) -> None:
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self) -> None:
        self.headvale = None

first_list = SLinkedList()

first_list.headvale = Node("Mon")

second_list = Node('Tue')


