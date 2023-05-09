
class Node:
    # default Node should be in current state
    def __init__(self, data_value=None):
        self.data_value = data_value
        self.next_value = None
       
#  now lets create first head value and relative methods

class SingleList:
    def __init__(self):
        self.head_value = None

    def print_list(self):
        print_value = self.head_value
        while print_value is not None:
            print(print_value.data_value)
            print_value = print_value.next_value


flist = SingleList()

flist.head_value = Node("Mon")
node2 = Node("Tue")
node3 = Node("Wed")

flist.head_value.next_value = node2

node3.next_value = node3

flist.print_list()






