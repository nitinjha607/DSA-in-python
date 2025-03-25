class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value): # Create new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self,value):  # Create new node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0           
    def prepend(self,value): # Create new node add node to beginning
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            # self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True         
        
    def insert(self,index,value): # Create new node and insert node 
        pass    
    def print_list(self): # Print the linked list we created 
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)
#print(my_linked_list.head.value) # Head and Tail pointer points to 4 node in this case
my_linked_list.prepend(1)
my_linked_list.prepend(2)
my_linked_list.prepend(3)
# my_linked_list.prepend(4)
# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)

print(my_linked_list.print_list())
