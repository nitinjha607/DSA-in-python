class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True            
    def get(self,index): # Method-2 Doubly Linked List Method
        if index <0 or index >= self.length:
            return None
        temp =self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev                
        return temp    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index ==0:
            return self.pop_first()
        if index ==self.length -1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        
        after.prev = before
        before.next = temp.next
        temp.next =None
        temp.prev = None
        
        self.length -=1
        return temp
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    

