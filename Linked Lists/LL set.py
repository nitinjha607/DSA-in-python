class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):
        if index <0 or index > self.length:
            return False
        if index ==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    def remove(self,index):
        if index <0 or index >= self.length:
            return None
        if index ==0:
            return self.pop_first()
        if index ==self.length-1:
            return self.pop()
        prev =self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp.value # To get value of element otherwise object will be returned
    def reverse(self):
        temp =self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after   
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            return slow
        return None             
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow ==fast:
                return True
        return False


my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1,4)

print('\nLL after set_value():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before set_value():
    11
    3
    23
    7

    LL after set_value():
    11
    4
    23
    7
"""