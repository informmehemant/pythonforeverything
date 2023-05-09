class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedlist:
    def __init__(self):
        self.headval = None
    # print the list
    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def at_begining(self, newdata):
        # new Node creations
        new_node = Node(newdata)
        # pointing new pointer to new_node.nextval -> self.headval
        new_node.nextval = self.headval

        self.headval = new_node

flist = SLinkedlist()

flist.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

flist.headval.nextval = e2
e2.nextval = e3
flist.print_list()
print("-----------")
flist.at_begining("Sun")
flist.print_list()
